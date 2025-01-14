# pylint: disable=too-many-lines, too-many-branches, too-many-statements
"""
Extract results from .castep file for comparison and use
by testcode.pl.

Port of extract_results.pl
"""

from collections import defaultdict
from typing import TextIO, List, Dict, Any, Union, Sequence, Tuple, Optional
import io
import re
import itertools

from . import castep_res as REs
from .castep_res import labelled_floats, get_numbers, get_block, gen_table_re

from .constants import SHELLS, ThreeVector, ThreeByThreeMatrix, AtomIndex

from .utility import (fix_data_types, add_aliases, to_type,
                      stack_dict, normalise_string,
                      atreg_to_index, log_factory)
from .extra_files_parser import (parse_bands_file,
                                 parse_hug_file,
                                 parse_phonon_dos_file,
                                 parse_efield_file,
                                 parse_xrd_sf_file,
                                 parse_elf_fmt_file,
                                 parse_chdiff_fmt_file,
                                 parse_pot_fmt_file,
                                 parse_den_fmt_file,
                                 parse_elastic_file)


def parse_castep_file(castep_file: TextIO) -> List[Dict[str, Any]]:
    """ Parse castep file into lists of dicts ready to JSONise """
    # pylint: disable=redefined-outer-name

    runs = []
    curr_run = defaultdict(list)

    logger = log_factory(castep_file)

    for line in castep_file:
        # Build Info
        if block := get_block(line, castep_file,
                              r"^\s*Compiled for",
                              REs.EMPTY, out_fmt=list):

            if curr_run:
                runs.append(curr_run)

            logger("Found build info")
            curr_run = defaultdict(list)
            curr_run["build_info"] = _process_buildinfo(block)

        elif re.search(r"Run started", line):
            curr_run["time_started"] = normalise_string(line.split(":", 1)[1])

            logger("Found run %s", len(runs) + 1)

        # Finalisation
        elif block := get_block(line, castep_file, "Initialisation time", REs.EMPTY):

            logger("Found finalisation")

            curr_run.update(_process_finalisation(block))

        elif line.startswith("Overall parallel efficiency rating"):

            logger("Found parallel efficiency")

            curr_run["parallel_efficiency"] = float(get_numbers(line)[0])

        # Title
        elif re.match(gen_table_re("Title", r"\*+"), line):

            logger("Found title")

            curr_run["title"] = next(castep_file).strip()

        # Memory estimate
        elif block := get_block(line, castep_file,
                                gen_table_re(r"MEMORY AND SCRATCH[\w\s]+", "[+-]+"),
                                gen_table_re("", "[+-]+")):

            logger("Found memory estimate")

            curr_run["memory_estimate"].append(_process_memory_est(block))

        # Parameters
        elif block := get_block(line, castep_file,
                                gen_table_re("[^*]+ Parameters", r"\*+"),
                                gen_table_re("", r"\*+")):

            logger("Found options")

            curr_run["options"] = _process_params(block)

        # Pseudo-atomic energy
        elif block := get_block(line, castep_file, REs.PS_SHELL_RE, REs.EMPTY, cnt=2):

            logger("Found pseudo-atomic energy")

            key, val = _process_ps_energy(block)

            if "species_properties" not in curr_run:
                curr_run["species_properties"] = defaultdict(dict)

            curr_run["species_properties"][key]["pseudo_atomic_energy"] = val

        # Mass
        elif block := get_block(line, castep_file, r"Mass of species in AMU", REs.EMPTY):

            logger("Found mass")

            if "species_properties" not in curr_run:
                curr_run["species_properties"] = defaultdict(dict)

            for key, val in _process_spec_prop(block):
                curr_run["species_properties"][key]["mass"] = float(val)

        # Electric Quadrupole Moment
        elif block := get_block(line, castep_file, r"Electric Quadrupole Moment", r"^\s+[^ A-Z]"):
            logger("Found electric quadrupole moment")

            if "species_properties" not in curr_run:
                curr_run["species_properties"] = defaultdict(dict)

            for key, val, *_ in _process_spec_prop(block):
                curr_run["species_properties"][key]["electric_quadrupole_moment"] = float(val)

        # Pseudopots
        elif block := get_block(line, castep_file, r"Files used for pseudopotentials", REs.EMPTY):

            logger("Found pseudopotentials")

            if "species_properties" not in curr_run:
                curr_run["species_properties"] = defaultdict(dict)

            for key, val in _process_spec_prop(block):
                if "|" in val:
                    val = _process_pspot_string(val)

                curr_run["species_properties"][key]["pseudopot"] = val

        elif block := get_block(line, castep_file,
                                gen_table_re("Pseudopotential Report[^|]+", r"\|"),
                                gen_table_re("", "=+")):

            logger("Found pseudopotential report")

            curr_run["pspot_detail"].append(_process_pspot_report(block))

        elif match := re.match(r"\s*(?P<type>AE|PS) eigenvalue nl (?P<nl>\d+) =" +
                               labelled_floats(('eigenvalue',)), line):

            logger("Found PSPot debug for %s at %s", match['type'], match['nl'])

            match = match.groupdict()
            fix_data_types(match, {'nl': int, 'eigenvalue': float})

            curr_run["pspot_debug"].append(match)

        # Pair Params
        elif block := get_block(line, castep_file,
                                gen_table_re("PairParams", r"\*+", pre=r"\w*"),
                                REs.EMPTY):

            logger("Found pair params")

            curr_run["pair_params"].append(_process_pair_params(block))

        # DFTD
        elif block := get_block(line, castep_file,
                                "DFT-D parameters",
                                gen_table_re("", "x+"), cnt=2):

            logger("Found DFTD block")

            curr_run["dftd"] = _process_dftd(block)

        # SCF
        elif block := get_block(line, castep_file, "SCF loop", "^-+ <-- SCF", cnt=2):

            logger("Found SCF")

            curr_run["scf"].append(_process_scf(block))

        # Line min
        elif block := get_block(line, castep_file,
                                gen_table_re("WAVEFUNCTION LINE MINIMISATION", "[+-]+",
                                             post="<- line"),
                                gen_table_re("", "[+-]+", post="<- line"), cnt=2):

            logger("Found wvfn line min")

            curr_run["wvfn_line_min"].append(_process_wvfn_line_min(block))

        # Occupancy
        elif block := get_block(line, castep_file,
                                gen_table_re("Occupancy", r"\|",
                                             post="<- occ", whole_line=False),
                                r"Have a nice day\."):

            logger("Found occupancies")

            curr_run["occupancies"].append(_process_occupancies(block))

        # Energies
        elif line.startswith("Final energy, E") or line.startswith("Final energy"):

            logger("Found energy")

            if "energies" not in curr_run:
                curr_run["energies"] = defaultdict(list)

            curr_run["energies"]["final_energy"].append(to_type(get_numbers(line)[-1], float))

        elif "Total energy corrected for finite basis set" in line:

            logger("Found energy")

            if "energies" not in curr_run:
                curr_run["energies"] = defaultdict(list)

            curr_run["energies"]["final_basis_set_corrected"].append(
                to_type(get_numbers(line)[-1], float))

        elif "0K energy (E-0.5TS)" in line:

            logger("Found estimated 0K energy")

            if "energies" not in curr_run:
                curr_run["energies"] = defaultdict(list)

            curr_run["energies"]["est_0K"].append(to_type(get_numbers(line)[-1], float))

        elif line.startswith("(SEDC) Total Energy"):

            logger("Found SEDC energy correction")

            if "energies" not in curr_run:
                curr_run["energies"] = defaultdict(list)

            curr_run["energies"]["sedc_correction"].append(to_type(get_numbers(line)[-1], float))

        elif line.startswith("Dispersion corrected final energy"):

            logger("Found SEDC final energy")

            if "energies" not in curr_run:
                curr_run["energies"] = defaultdict(list)

            curr_run["energies"]["disperson_corrected"].append(
                to_type(get_numbers(line)[-1], float))

        # Free energies
        elif re.match(rf"Final free energy \(E-TS\) += +({REs.EXPNUMBER_RE})", line):

            logger("Found free energy (E-TS)")

            if "energies" not in curr_run:
                curr_run["energies"] = defaultdict(list)

            curr_run["energies"]["free_energy"].append(to_type(get_numbers(line)[-1], float))

        # Solvation energy
        elif line.startswith(" Free energy of solvation"):

            logger("Found solvation energy")

            if "energies" not in curr_run:
                curr_run["energies"] = defaultdict(list)

            curr_run["energies"]["solvation"].append(*to_type(get_numbers(line), float))

        # Spin densities
        elif match := re.search(rf"Integrated \|?Spin Density\|?\s+=\s+({REs.EXPNUMBER_RE})", line):

            logger("Found spin")

            if "|" in line:
                curr_run["modspin"].append(to_type(match.group(1), float))
            else:
                curr_run["spin"].append(to_type(match.group(1), float))

        # Initial cell
        elif block := get_block(line, castep_file, gen_table_re("Unit Cell"), REs.EMPTY, cnt=3):

            logger("Found cell")

            curr_run["initial_cell"] = _process_unit_cell(block)

        # Cell Symmetry and contstraints
        elif block := get_block(line, castep_file,
                                gen_table_re("Symmetry and Constraints"),
                                "Cell constraints are"):

            logger("Found symmetries")

            curr_run["symmetries"], curr_run["constraints"] = _process_symmetry(block)

        # TSS (must be ahead of initial pos)
        elif block := get_block(line, castep_file,
                                gen_table_re("(Reactant|Product)", "x"),
                                gen_table_re("", "x+"), cnt=2):

            mode = "reactant" if "Reactant" in line else "product"

            logger("Found %s initial states", mode)

            curr_run[mode] = _process_atreg_block(block)

        # Initial pos
        elif block := get_block(line, castep_file,
                                "Fractional coordinates of atoms",
                                gen_table_re("", "x+")):

            logger("Found initial positions")

            curr_run["initial_positions"] = _process_atreg_block(block)

        elif "Supercell generated" in line:
            accum = iter(get_numbers(line))
            curr_run["supercell"] = tuple(to_type([next(accum) for _ in range(3)], float)
                                          for _ in range(3))

        # Initial vel
        elif block := get_block(line, castep_file,
                                "User Supplied Ionic Velocities",
                                gen_table_re("", "x+")):

            logger("Found initial velocities")

            curr_run["initial_velocities"] = _process_atreg_block(block)

        # Initial spins
        elif block := get_block(line, castep_file,
                                "Initial magnetic",
                                gen_table_re("", "x+")):

            logger("Found initial spins")

            curr_run["initial_spins"] = _process_initial_spins(block)

        # Target Stress
        elif block := get_block(line, castep_file, "External pressure/stress", REs.EMPTY):

            logger("Found target stress")

            curr_run["target_stress"].extend(number
                                             for line in block
                                             for number in to_type(get_numbers(line), float))

        # Finite basis correction parameter
        elif match := re.search(rf"finite basis dEtot\/dlog\(Ecut\) = +({REs.FNUMBER_RE})", line):

            logger("Found dE/dlog(E)")
            curr_run["dedlne"].append(to_type(match.group(1), float))

        # K-Points
        elif block := get_block(line, castep_file, "k-Points For BZ Sampling", REs.EMPTY):

            logger("Found k-points")

            curr_run["k-points"] = _process_kpoint_blocks(block, True)

        elif block := get_block(line, castep_file,
                                gen_table_re("Number +Fractional coordinates +Weight", r"\+"),
                                gen_table_re("", r"\++")):

            logger("Found k-points list")

            curr_run["k-points"] = _process_kpoint_blocks(block, False)

        # Forces blocks
        elif block := get_block(line, castep_file, REs.FORCES_BLOCK_RE, r"^\s*\*+$"):
            if "forces" not in curr_run:
                curr_run["forces"] = defaultdict(list)

            key, val = _process_forces(block)

            logger("Found %s forces", key)

            curr_run["forces"][key].append(val)

        # Stress tensor block
        elif block := get_block(line, castep_file, REs.STRESSES_BLOCK_RE, r"^\s*\*+$"):
            if "stresses" not in curr_run:
                curr_run["stresses"] = defaultdict(list)

            key, val = _process_stresses(block)

            logger("Found %s stress", key)

            curr_run["stresses"][key].append(val)

        # Phonon block
        elif match := REs.PHONON_RE.match(line):

            logger("Found phonon")

            qdata = defaultdict(list)

            qdata["qpt"] = match.group("qpt").split()

            logger("Reading qpt %s", qdata['qpt'], level="debug")

            for line in castep_file:
                if match := REs.PHONON_RE.match(line):
                    if qdata["qpt"] and qdata["qpt"] not in (phonon["qpt"]
                                                             for phonon in curr_run["phonons"]):
                        curr_run["phonons"].append(_process_qdata(qdata))
                    qdata = defaultdict(list)
                    qdata["qpt"] = match.group("qpt").split()

                    logger("Reading qpt %s", qdata['qpt'], level="debug")

                elif (re.match(r"\s+\+\s+Effective cut-off =", line) or
                      re.match(rf"\s+\+\s+q->0 along \((\s*{REs.FNUMBER_RE}){{3}}\)\s+\+", line) or
                      re.match(r"\s+\+ -+ \+", line)):
                    continue
                elif match := REs.PROCESS_PHONON_RE.match(line):

                    # ==By mode
                    # qdata["modes"].append(match.groupdict())
                    # ==By prop
                    stack_dict(qdata, match.groupdict())

                elif re.match(r"\s+\+\s+.*\+", line):
                    continue
                else:
                    break

            else:
                raise IOError(f"Unexpected end of file in {castep_file.name}")

            if qdata["qpt"] and qdata["qpt"] not in (phonon["qpt"]
                                                     for phonon in curr_run["phonons"]):
                curr_run["phonons"].append(_process_qdata(qdata))

            logger("Found %d phonon samples", len(curr_run['phonons']))

        # Phonon Symmetry
        elif block := get_block(line, castep_file,
                                "Phonon Symmetry Analysis", REs.EMPTY):

            logger("Found phonon symmetry analysis")

            val = _process_phonon_sym_analysis(block)
            curr_run["phonon_symmetry_analysis"].append(val)

            # Solvation
        elif block := get_block(line, castep_file,
                                gen_table_re("AUTOSOLVATION CALCULATION RESULTS", r"\*+"),
                                r"^\s*\*+\s*$"):

            logger("Found autosolvation")

            curr_run["autosolvation"] = _process_autosolvation(block)

        # Dynamical Matrix
        elif block := get_block(line, castep_file,
                                gen_table_re("Dynamical matrix"),
                                gen_table_re("", "-+")):

            logger("Found dynamical matrix")

            val = _process_dynamical_matrix(block)
            curr_run["dynamical_matrix"] = val

        # Raman tensors
        elif block := get_block(line, castep_file,
                                gen_table_re("Raman Susceptibility Tensors[^+]*", r"\+"),
                                REs.EMPTY):

            logger("Found Raman")

            curr_run["raman"].append(_process_raman(block))

        # Born charges
        elif block := get_block(line, castep_file,
                                gen_table_re("Born Effective Charges"),
                                gen_table_re("", "=+")):

            logger("Found Born")

            curr_run["born"].append(_process_born(block))

        # Permittivity and NLO Susceptibility
        elif block := get_block(line, castep_file,
                                r"^\s+Optical Permittivity", r"^ =+$"):

            logger("Found optical permittivity")

            val = _process_3_6_matrix(block, True)
            curr_run["optical_permittivity"] = val[0]
            if val[1]:
                curr_run["dc_permittivity"] = val[1]

        # Polarisability
        elif block := get_block(line, castep_file, r"^\s+Polarisabilit(y|ies)", r"^ =+$"):

            logger("Found polarisability")

            val = _process_3_6_matrix(block, True)
            curr_run["optical_polarisability"] = val[0]
            if val[1]:
                curr_run["static_polarisability"] = val[1]

        # Non-linear
        elif block := get_block(line, castep_file,
                                r"^\s+Nonlinear Optical Susceptibility", r"^ =+$"):

            logger("Found NLO")

            curr_run["nlo"], _ = _process_3_6_matrix(block, False)

        # Thermodynamics
        elif block := get_block(line, castep_file,
                                gen_table_re("Thermodynamics"),
                                gen_table_re("", "-+"), cnt=3):

            logger("Found thermodynamics")

            accum = _process_thermodynamics(block)
            curr_run["thermodynamics"] = accum

        # Mulliken Population Analysis
        elif block := get_block(line, castep_file,
                                gen_table_re(r"Atomic Populations \(Mulliken\)"),
                                gen_table_re("", "=+"), cnt=2):

            logger("Found Mulliken")

            curr_run["mulliken_popn"] = _process_mulliken(block)

        # Orbital populations
        elif block := get_block(line, castep_file,
                                gen_table_re("Orbital Populations"),
                                "The total projected population"):

            logger("Found Orbital populations")

            curr_run["orbital_popn"] = _process_orbital_populations(block)

        # Bond analysis
        elif block := get_block(line, castep_file,
                                r"Bond\s+Population\s+Length",
                                gen_table_re("", "=+"), cnt=2):

            logger("Found bond info")

            curr_run["bonds"] = _process_bond_analysis(block)

        # Hirshfeld Population Analysis
        elif block := get_block(line, castep_file,
                                gen_table_re("Hirshfeld Analysis"),
                                gen_table_re("", "=+"), cnt=2):

            logger("Found Hirshfeld")

            curr_run["hirshfeld"] = _process_hirshfeld(block)

        # ELF
        elif block := get_block(line, castep_file,
                                gen_table_re("ELF grid sample"),
                                gen_table_re("", "-+"), cnt=2):

            logger("Found ELF")

            curr_run["elf"] = _process_elf(block)

        # MD Block
        elif block := get_block(line, castep_file,
                                gen_table_re("MD Data:", "x"),
                                gen_table_re("", "x+")):

            logger("Found MD Block (step %d)", len(curr_run['md'])+1)

            curr_run["md"].append(_process_md(block))

        # GeomOpt
        elif block := get_block(line, castep_file, "Final Configuration",
                                gen_table_re("", "x+"), cnt=2):

            if "geom_opt" not in curr_run:
                curr_run["geom_opt"] = defaultdict(list)

            logger("Found final geom configuration")

            curr_run["geom_opt"]["final_configuration"] = _process_atreg_block(block)

        elif match := re.search(f"(?P<minim>{REs.MINIMISERS_RE}):"
                                r" finished iteration\s*\d+\s*with enthalpy", line):

            if "geom_opt" not in curr_run:
                curr_run["geom_opt"] = defaultdict(list)

            minim = match["minim"]

            logger("Found %s energy", minim)

            curr_run["geom_opt"]["enthalpy"].append(to_type(get_numbers(line)[-1], float))

        elif match := re.match(rf"^\s*(?:{REs.MINIMISERS_RE}):"
                               r"(?P<key>[^=]+)=\s*"
                               f"(?P<value>{REs.EXPNUMBER_RE}).*",
                               line, re.IGNORECASE):

            if "geom_opt" not in curr_run:
                curr_run["geom_opt"] = defaultdict(list)

            key, val = normalise_string(match["key"]).lower(), to_type(match["value"], float)

            logger("Found geomopt %s", key)

            curr_run["geom_opt"][key] = val

        elif block := get_block(line, castep_file,
                                f"<--( min)? {REs.MINIMISERS_RE}$", r"\+(?:-+\+){4,5}", cnt=2):

            typ = re.search(REs.MINIMISERS_RE, line).group(0)

            if "geom_opt" not in curr_run:
                curr_run["geom_opt"] = defaultdict(list)

            logger("Found %s geom_block", typ)

            curr_run["geom_opt"]["minimisation"].append(_process_geom_table(block))

        # TDDFT
        elif block := get_block(line, castep_file,
                                gen_table_re("TDDFT excitation energies", r"\+", post="TDDFT"),
                                gen_table_re("=+", r"\+", post="TDDFT"), cnt=2):

            logger("Found TDDFT excitations")

            curr_run["tddft"] = _process_tddft(block)

        # Band structure
        elif block := get_block(line, castep_file,
                                gen_table_re("(B A N D|Band Structure Calculation)[^+]+", r"\+"),
                                gen_table_re("", "=+")):

            logger("Found band-structure")

            curr_run["bs"] = _process_band_structure(block)

            # Molecular Dipole
        elif block := get_block(line, castep_file,
                                gen_table_re("D I P O L E   O F   M O L E C U L E"
                                             "   I N   S U P E R C E L L",
                                             r"\+"),
                                gen_table_re("", "=+")):

            logger("Found molecular dipole")

            curr_run["molecular_dipole"] = _process_dipole(block)

        # Chemical shielding
        elif block := get_block(line, castep_file,
                                gen_table_re("Chemical Shielding Tensor", r"\|"),
                                gen_table_re("", "=+")):

            logger("Found Chemical Shielding Tensor")

            val = _parse_magres_block(0, block)
            curr_run["magres"].append(val)

        elif block := get_block(line, castep_file,
                                gen_table_re("Chemical Shielding and "
                                             "Electric Field Gradient Tensors", r"\|"),
                                gen_table_re("", "=+")):

            logger("Found Chemical Shielding + EField Tensor")

            val = _parse_magres_block(1, block)
            curr_run["magres"].append(val)

        elif block := get_block(line, castep_file,
                                gen_table_re("Electric Field Gradient Tensor", r"\|"),
                                gen_table_re("", "=+")):

            logger("Found EField Tensor")

            val = _parse_magres_block(2, block)
            curr_run["magres"].append(val)

        elif block := get_block(line, castep_file,
                                gen_table_re("(?:I|Ani)sotropic J-coupling", r"\|"),
                                gen_table_re("", "=+")):

            logger("Found J-coupling")

            val = _parse_magres_block(3, block)
            curr_run["magres"].append(val)

        elif block := get_block(line, castep_file,
                                gen_table_re("Hyperfine Tensor", r"\|"),
                                gen_table_re("", "=+")):

            logger("Found Hyperfine tensor")

            val = _parse_magres_block(4, block)
            curr_run["magres"].append(val)

        # Elastic
        elif block := get_block(line, castep_file,
                                gen_table_re(r"Elastic Constants Tensor \(GPa\)"),
                                gen_table_re("", "=+")):

            logger("Found elastic constants tensor")

            if "elastic" not in curr_run:
                curr_run["elastic"] = {}
            val, _ = _process_3_6_matrix(block, False)
            curr_run["elastic"]["elastic_constants"] = val

        elif block := get_block(line, castep_file,
                                gen_table_re(r"Compliance Matrix \(GPa\^-1\)"),
                                gen_table_re("", "=+")):

            logger("Found compliance matrix")

            if "elastic" not in curr_run:
                curr_run["elastic"] = {}
            val, _ = _process_3_6_matrix(block, False)
            curr_run["elastic"]["compliance_matrix"] = val

        elif block := get_block(line, castep_file, "Contribution ::", REs.EMPTY):
            typ = re.match("(?P<type>.* Contribution)", line).group("type")
            next(block)

            logger("Found elastic %s contribution", typ)

            if "elastic" not in curr_run:
                curr_run["elastic"] = {}

            val, _ = _process_3_6_matrix(block, False)
            curr_run["elastic"][typ] = val

        elif block := get_block(line, castep_file,
                                gen_table_re("Elastic Properties"),
                                gen_table_re("", "=+")):

            logger("Found elastic properties")

            if "elastic" not in curr_run:
                curr_run["elastic"] = {}

            curr_run["elastic"].update(_process_elastic_properties(block))

        # --- Extra blocks for testing

        # Hugoniot data
        elif block := get_block(line, castep_file, "BEGIN hug", "END hug"):

            logger("Found hug block")

            val = parse_hug_file(block)
            curr_run["hug"].append(val)

        # Bands block (spectral data)
        elif block := get_block(line, castep_file, "BEGIN bands", "END bands"):

            logger("Found bands block")

            val = parse_bands_file(block)
            curr_run["bands"].append(val["bands"])

        elif block := get_block(line, castep_file, "BEGIN phonon_dos", "END phonon_dos"):

            logger("Found phonon_dos block")

            val = parse_phonon_dos_file(block)
            curr_run["phonon_dos"] = val["dos"]
            curr_run["gradients"] = val["gradients"]

        # E-Field
        elif block := get_block(line, castep_file, "BEGIN efield", "END efield"):

            logger("Found efield block")

            val = parse_efield_file(block)
            curr_run["oscillator_strengths"] = val["oscillator_strengths"]
            curr_run["permittivity"] = val["permittivity"]

        # Elastic
        elif block := get_block(line, castep_file, "<BEGIN elastic>", "<END elastic>"):

            logger("Found elastic block")

            val = parse_elastic_file(block)
            curr_run["oscillator_strengths"] = val["elastic_constants"]
            curr_run["permittivity"] = val["compliance_matrix"]

        # XRD Structure Factor
        elif block := get_block(line, castep_file, "BEGIN xrd_sf", "END xrd_sf",
                                out_fmt=list):

            logger("Found xrdsf")

            block = "\n".join(block[1:-1])  # Strip begin/end tags lazily
            block = io.StringIO(block)
            val = parse_xrd_sf_file(block)

            curr_run["xrd_sf"] = val

        # ELF FMT
        elif block := get_block(line, castep_file, "BEGIN elf_fmt", "END elf_fmt",
                                out_fmt=list):

            logger("Found ELF fmt")

            block = "\n".join(block[1:-1])  # Strip begin/end tags lazily
            block = io.StringIO(block)
            val = parse_elf_fmt_file(block)
            if "kpt-data" not in curr_run:
                curr_run["kpt-data"] = val
            else:
                curr_run["kpt-data"].update(val)

        # CHDIFF FMT
        elif block := get_block(line, castep_file, "BEGIN chdiff_fmt", "END chdiff_fmt",
                                out_fmt=list):

            logger("Found CHDIFF fmt")

            block = "\n".join(block[1:-1])  # Strip begin/end tags lazily
            block = io.StringIO(block)
            val = parse_chdiff_fmt_file(block)
            if "kpt-data" not in curr_run:
                curr_run["kpt-data"] = val
            else:
                curr_run["kpt-data"].update(val)

        # POT FMT
        elif block := get_block(line, castep_file, "BEGIN pot_fmt", "END pot_fmt",
                                out_fmt=list):

            logger("Found POT fmt")

            block = "\n".join(block[1:-1])  # Strip begin/end tags lazily
            block = io.StringIO(block)
            val = parse_pot_fmt_file(block)
            if "kpt-data" not in curr_run:
                curr_run["kpt-data"] = val
            else:
                curr_run["kpt-data"].update(val)

        # DEN FMT
        elif block := get_block(line, castep_file, "BEGIN den_fmt", "END den_fmt",
                                out_fmt=list):

            logger("Found DEN fmt")

            block = "\n".join(block[1:-1])  # Strip begin/end tags lazily
            block = io.StringIO(block)
            val = parse_den_fmt_file(block)
            if "kpt-data" not in curr_run:
                curr_run["kpt-data"] = val
            else:
                curr_run["kpt-data"].update(val)

    if curr_run:
        fix_data_types(curr_run, {"energies": float,
                                  "solvation": float})
        runs.append(curr_run)
    return runs


def _process_ps_energy(block: TextIO) -> Tuple[str, float]:
    match = REs.PS_SHELL_RE.search(next(block))
    spec = match["spec"]
    next(block)
    energy = get_numbers(next(block))[1]
    return spec, float(energy)


def _process_tddft(block: TextIO) -> List[Dict[str, Union[str, float]]]:
    tddata = [{"energy": float(match["energy"]),
               "error": float(match["error"]),
               "type": match["type"]}
              for line in block
              if (match := REs.TDDFT_RE.match(line))]
    return tddata


def _process_atreg_block(block: TextIO) -> Dict[AtomIndex, ThreeVector]:
    accum = {atreg_to_index(match): to_type(match.group("x", "y", "z"), float)
             for line in block
             if (match := REs.ATDAT3VEC.search(line))}
    return accum


def _process_spec_prop(block: TextIO) -> List[List[str]]:

    accum = []

    for line in block:
        words = line.split()
        if words and re.match(rf"{REs.SPECIES_RE}\b", words[0]):

            accum.append(words)

    return accum


def _process_md(block: TextIO) -> Dict[str, float]:
    curr_data = {match.group("key").strip(): float(match.group("val"))
                 for line in block
                 if (match := re.search(r"x\s+"
                                        r"(?P<key>[a-zA-Z][A-Za-z ]+):\s*"
                                        rf"(?P<val>{REs.FNUMBER_RE})", line))}

    return {normalise_string(key): val for key, val in curr_data.items()}


def _process_elf(block: TextIO) -> List[float]:
    curr_data = [to_type(match.group(1), float) for line in block
                 if (match := re.match(rf"\s+ELF\s+\d+\s+({REs.FNUMBER_RE})", line))]
    return curr_data


def _process_hirshfeld(block: TextIO) -> Dict[AtomIndex, float]:
    """ Process Hirshfeld block to dict of charges """
    accum = {atreg_to_index(match): float(match["charge"]) for line in block
             if (match := re.match(rf"\s+{REs.ATREG}\s+(?P<charge>{REs.FNUMBER_RE})", line))}
    return accum


def _process_thermodynamics(block: TextIO) -> Dict[str, List[float]]:
    """ Process a thermodynamics block into a dict of lists """
    accum = defaultdict(list)
    for line in block:
        if "Zero-point energy" in line:
            accum["zero-point_energy"] = float(get_numbers(line)[0])

        if match := REs.THERMODYNAMICS_DATA_RE.match(line):
            stack_dict(accum, match.groupdict())
        # elif re.match(r"\s+T\(", line):  # Can make dict/re based on labels
        #     thermo_label = line.split()

    fix_data_types(accum, {key: float for
                           key in ("T", "E", "F", "S", "Cv")})
    return accum


def _process_3_6_matrix(block: TextIO, split: bool) -> Tuple[ThreeByThreeMatrix,
                                                             Optional[ThreeByThreeMatrix]]:
    """ Process a single or pair of 3x3 matrices or 3x6 matrix """
    fst = [to_type(vals, float) for line in block
           if (vals := get_numbers(line)) and len(vals) in (3, 6)]
    if split and len(fst[0]) == 6:
        fst, snd = [tuple(line[0:3]) for line in fst], [tuple(line[3:6]) for line in fst]
    else:
        snd = []

    return fst, snd


def _process_params(block: TextIO) -> Dict[str, str]:
    """ Process a parameters block into a dict of params """

    opt = {}
    curr_opt = {}
    curr_group = ""

    for line in block:
        if match := re.match(r"\s*\*+ ([A-Za-z ]+) Parameters \*+", line):
            if curr_opt:
                opt[curr_group] = curr_opt
            curr_group = normalise_string(match.group(1)).lower()
            curr_opt = {}
        elif len(match := line.split(":")) > 1:
            *key, val = map(normalise_string, match)
            curr_opt[" ".join(key).strip()] = val.strip()

    if curr_opt:
        opt[curr_group] = curr_opt

    return opt


def _process_buildinfo(block: Sequence[str]) -> Dict[str, str]:
    info = {}

    info["summary"] = " ".join(map(normalise_string, block[0:2]))
    for line in block[2:]:
        if ":" in line:
            key, val = map(normalise_string, line.split(":", 1))
            info[key.strip()] = val.strip()
    return info


def _process_unit_cell(block: TextIO) -> Dict[str, Union[ThreeVector, ThreeByThreeMatrix]]:
    cell = defaultdict(list)
    prop = []
    for line in block:
        numbers = get_numbers(line)
        if len(numbers) == 6:
            cell["real_lattice"].append(to_type(numbers[0:3], float))
            cell["recip_lattice"].append(to_type(numbers[3:6], float))
        elif len(numbers) == 2:
            if any(ang in line for ang in ("alpha", "beta", "gamma")):
                cell["lattice_parameters"].append(to_type(numbers[0], float))
                cell["cell_angles"].append(to_type(numbers[1], float))
            else:
                prop.append(to_type(numbers[0], float))

    cell.update({name: val for val, name in zip(prop, ("volume", "density_amu", "density_g"))})

    return cell


def _process_scf(block: TextIO) -> Dict[str, Any]:
    scf = []
    curr = {}
    for line in block:
        if match := REs.SCF_LOOP_RE.match(line):
            if curr:
                scf.append(curr)
            curr = match.groupdict()
            fix_data_types(curr, {"energy": float,
                                  "energy_gain": float,
                                  "fermi_energy": float,
                                  "time": float})

        elif "Density was not mixed" in line:
            curr["density_residual"] = None

        elif "Norm of density" in line:
            curr["density_residual"] = to_type(get_numbers(line)[0], float)

        elif "no. bands" in line:
            curr["no_bands"] = to_type(get_numbers(line)[0], int)

        elif "Kinetic eigenvalue" in line:
            if "kinetic_eigenvalue" not in curr:
                curr["kinetic_eigenvalue"] = []
                curr["eigenvalue"] = []

            curr["kinetic_eigenvalue"] = to_type(get_numbers(line)[1], float)
            eig = []

        elif re.match(r"eigenvalue\s*\d+\s*init=", line):
            labels = ("initial", "final", "change")
            numbers = get_numbers(line)
            eig.append({key: float(val) for val, key in zip(numbers[1:], labels)})

        elif "Checking convergence criteria" in line:
            curr["eigenvalue"].append(eig)
            eig = []

        elif match := re.match(r"[+(]?(?P<key>[()0-9A-Za-z -]+)="
                               rf"\s*{labelled_floats(('val',))} eV\)?", line):
            key, val = normalise_string(match["key"]).lower(), float(match["val"])
            curr[key] = val

    if curr:
        scf.append(curr)

    return scf


def _process_forces(block: TextIO) -> Tuple[str, Dict[AtomIndex, ThreeVector]]:
    ftype = (ft_guess if (ft_guess := REs.FORCES_BLOCK_RE.search(next(block)).group(1))
             else "non-descript")

    ftype = normalise_string(ftype).lower()

    accum = _process_atreg_block(block)

    return ftype, accum


def _process_stresses(block: TextIO) -> Tuple[float]:

    ftype = (ft_guess if (ft_guess := REs.STRESSES_BLOCK_RE.search(next(block)).group(1))
             else "non-descript")

    ftype = normalise_string(ftype).lower()

    accum = []
    for line in block:
        numbers = get_numbers(line)
        if "*  x" in line:
            accum += numbers[0:]
        elif "*  y" in line:
            accum += numbers[1:]
        elif "*  z" in line:
            accum += numbers[2:]

    accum = to_type(accum, float)

    return ftype, accum


def _process_initial_spins(block: TextIO) -> Dict[AtomIndex, Union[float, bool]]:

    accum = {}
    for line in block:
        if match := re.match(rf"\s*\|\s*{REs.ATREG}\s*"
                             rf"{labelled_floats(('spin', 'magmom'))}\s*"
                             r"(?P<fix>[TF])\s*\|", line):
            match = match.groupdict()
            ind = atreg_to_index(match)
            fix_data_types(match, {"spin": float, "magmom": float})
            match["fix"] = match["fix"] == "T"
            accum[ind] = match
    return accum


def _process_born(block: TextIO) -> Dict[AtomIndex, ThreeByThreeMatrix]:
    """ Process a Born block into a dict of charges """

    born_accum = {}
    for line in block:
        if match := REs.BORN_RE.match(line):
            born_accum[atreg_to_index(match)] = (to_type(match["charges"].split(), float),
                                                 to_type(next(block).split(), float),
                                                 to_type(next(block).split(), float))
    return born_accum


def _process_raman(block: TextIO) -> List[Dict[str, Union[ThreeVector, ThreeByThreeMatrix]]]:
    """ Process a Mulliken block into a list of modes """

    next(block)  # Skip first captured line
    modes = []
    curr_mode = {}
    for line in block:
        if "Mode number" in line:
            if curr_mode:
                modes.append(curr_mode)
            curr_mode = {"tensor": [], "depolarisation": None}
        elif numbers := get_numbers(line):
            curr_mode["tensor"].append(to_type(numbers[0:3], float))
            if len(numbers) == 4:
                curr_mode["depolarisation"] = to_type(numbers[3], float)

        elif re.search(r"^ \+\s+\+", line):  # End of 3x3+depol block
            # Compute Invariants Tr(A) and Tr(A)^2-Tr(A^2) of Raman Tensor
            curr_mode["tensor"] = tuple(curr_mode["tensor"])
            tensor = curr_mode["tensor"]
            curr_mode["trace"] = sum(tensor[i][i] for i in range(3))
            curr_mode["II"] = (tensor[0][0]*tensor[1][1] +
                               tensor[0][0]*tensor[2][2] +
                               tensor[1][1]*tensor[2][2] -
                               tensor[0][1]*tensor[1][0] -
                               tensor[0][2]*tensor[2][0] -
                               tensor[1][2]*tensor[2][1])
    if curr_mode:
        modes.append(curr_mode)

    return modes


def _process_mulliken(block: TextIO) -> Dict[AtomIndex, Dict[str, float]]:
    """ Process a mulliken block into a dict of points """
    accum = {}

    for line in block:
        if match := REs.POPN_RE.match(line):
            mull = match.groupdict()
            mull["spin_sep"] = bool(mull["spin_sep"])
            if mull["spin_sep"]:  # We have spin separation
                add_aliases(mull,
                            {orb: f"up_{orb}" for orb in (*SHELLS, "total")},
                            replace=True)
                line = next(block)
                match = REs.POPN_RE_DN.match(line)
                match = match.groupdict()

                add_aliases(match,
                            {orb: f"dn_{orb}" for orb in (*SHELLS, "total")},
                            replace=True)

                mull.update(match)
                mull["total"] = float(mull["up_total"]) + float(mull["dn_total"])

            ind = atreg_to_index(mull)
            fix_data_types(mull, {**{f"{orb}": float for orb in (*SHELLS, "total",
                                                                 "charge", "spin")},
                                  **{f"up_{orb}": float for orb in (*SHELLS, "total")},
                                  **{f"dn_{orb}": float for orb in (*SHELLS, "total")}})
            accum[ind] = mull

    return accum


def _process_band_structure(block: TextIO) -> List[Dict[str, Union[float, int]]]:
    """ Process a band structure into a list of kpts"""

    def fdt(qdat):
        fix_data_types(qdat, {"spin": int,
                              "kx": float,
                              "ky": float,
                              "kz": float,
                              "kpgrp": int,
                              "band": int,
                              "energy": float})

    bands = []
    qdata = {}

    for line in block:
        if match := REs.BS_RE.search(line):
            if qdata:
                fdt(qdata)
                bands.append(qdata)
            qdata = {"band": [], "energy": [], **match.groupdict()}

        elif match := re.search(labelled_floats(("band", "energy"), sep=r"\s+"), line):
            stack_dict(qdata, match.groupdict())

    if qdata:
        fdt(qdata)
        bands.append(qdata)

    return bands


def _process_qdata(qdata: Dict[str, str]) -> Dict[str, Union[float, int]]:
    """ Special parse for phonon qdata """
    qdata = {key: val
             for key, val in qdata.items()
             if any(val) or key == "qpt"}
    fix_data_types(qdata,
                   {"qpt": float,
                    "N": int,
                    "frequency": float,
                    "intensity": float,
                    "raman_intensity": float
                    })
    return qdata


def _parse_magres_block(task: int, inp: TextIO) -> Dict[str, Dict[AtomIndex, float]]:
    """ Parse MagRes data tables from inp according to task """

    data = defaultdict(list)
    data["task"] = REs.MAGRES_TASK[task]
    curr_re = REs.MAGRES_RE[task]
    for line in inp:
        if match := curr_re.match(line):
            match = match.groupdict()
            ind = atreg_to_index(match)
            fix_data_types(match, {key: float for key in ("iso", "aniso", "cq", "eta",
                                                          "fc", "sd", "para", "dia", "tot")})

            if "asym" in match:
                match["asym"] = float(match["asym"]) if match["asym"] != "N/A" else None

            data[ind] = match

    return data


def _process_finalisation(block: TextIO) -> Dict[str, float]:

    out = {}

    for line in block:
        if line.strip():
            key, val = line.split("=")
            out[normalise_string(key.lower())] = to_type(get_numbers(val)[0], float)
    return out


def _process_memory_est(block: TextIO) -> Dict[str, float]:

    accum = {}

    for line in block:
        if match := re.match(r"\s*\|([A-Za-z ]+)" +
                             labelled_floats(("memory", "disk"), suff=" MB"), line):
            key, memory, disk = match.groups()
            accum[normalise_string(key)] = {"memory": float(memory),
                                            "disk": float(disk)}

    return accum


def _process_phonon_sym_analysis(block: TextIO) -> Dict[str, Union[str, List[List[float]]]]:

    accum = {}
    accum["title"] = normalise_string(next(block).split(":")[1])
    next(block)
    accum["mat"] = [to_type(numbers, int) if all(map(lambda x: x.isdigit(), numbers))
                    else to_type(numbers, float)
                    for line in block if (numbers := get_numbers(line))]
    return accum


def _process_kpoint_blocks(block: TextIO,
                           explicit_kpoints: bool) -> Dict[str, Union[ThreeVector, float, int]]:

    if explicit_kpoints:
        accum = {}
        for line in block:
            if "MP grid size" in line:
                accum["kpoint_mp_grid"] = to_type(get_numbers(line), int)
            elif "offset" in line:
                accum["kpoint_mp_offset"] = to_type(get_numbers(line), float)
            elif "Number of kpoints" in line:
                accum["num_kpoints"] = to_type(get_numbers(line)[0], int)
    else:

        accum = {'points': [{"qpt": to_type(match.group("qx", "qy", "qx"), float),
                             "weight": to_type(match["wt"], float)}
                            for line in block
                            if (match :=
                                re.match(
                                    gen_table_re(r"\d\s*" +
                                                 labelled_floats(('qx', 'qy', 'qz', 'wt')), r"\+"),
                                    line))]}
        accum["num_kpoints"] = len(accum["points"])

    return accum


def _process_symmetry(block: TextIO) -> Dict[str, Any]:

    sym = {}
    con = {}

    for line in block:
        if "=" in line:
            key, val = map(normalise_string, line.split("="))

            if "Number of" in line:
                val = to_type(val, int)

            if "constraints" in key:
                con[key] = val
            else:
                sym[key] = val

        elif re.match(r"\s*\d+\s*rotation\s*", line):
            if "symop" not in sym:
                sym["symop"] = []

            curr_sym = {"rotation": [], "symmetry_related": []}
            for curr_ln in itertools.islice(block, 3):
                curr_sym["rotation"].append(to_type(get_numbers(curr_ln), float))

            next(block)  # elif re.match(r"\s*\d+\s*displacement\s*", line):

            curr_sym["displacement"] = to_type(get_numbers(next(block)), float)

            next(block)  # elif "symmetry related atoms:" in line:

            while line := next(block).strip():
                key, val = line.split(":")
                curr_sym["symmetry_related"].extend((key, int(ind))
                                                    for ind in val.split())

            sym['symop'].append(curr_sym)

        elif "Centre of mass" in line:
            con["com_constrained"] = "NOT" not in line

        elif cons_block := get_block(line, block,
                                     r"constraints\.{5}", r"\s*x+\.{4}\s*", out_fmt=str):
            con["ionic_constraints"] = defaultdict(list)
            for match in re.finditer(rf"{REs.ATREG}\s*[xyz]\s*" +
                                     labelled_floats(('pos',), counts=(3,)),
                                     cons_block):
                match = match.groupdict()
                ind = atreg_to_index(match)
                con["ionic_constraints"][ind].append(to_type(match["pos"].split(), float))
        elif "Cell constraints are:" in line:
            con["cell_constraints"] = to_type(get_numbers(line), int)

    return sym, con


def _process_dynamical_matrix(block: TextIO) -> Tuple[complex]:
    next(block)  # Skip header line
    next(block)

    real_part = []
    for line in block:
        if "Ion" in line:
            break
        numbers = get_numbers(line)
        real_part.append(numbers[2:])

    imag_part = []
    # Get remainder
    for line in block:
        if numbers := get_numbers(line):
            imag_part.append(numbers[2:])

    accum = []
    for real_row, imag_row in zip(real_part, imag_part):
        accum.append(tuple(complex(float(real), float(imag))
                           for real, imag in zip(real_row, imag_row)))

    return tuple(accum)


def _process_pspot_string(string: str) -> Dict[str, Union[float, int, str]]:
    if not (match := REs.PSPOT_RE.match(string)):
        raise IOError(f"Attempt to parse {string} as PSPot failed")

    pspot = match.groupdict()
    projectors = []
    for proj in pspot["proj"].split(":"):
        pdict = REs.PSPOT_PROJ_RE.match(proj).groupdict()
        pdict["shell"] = SHELLS[int(pdict["shell"])]
        fix_data_types(pdict, {"orbital": int})
        projectors.append(pdict)

    if not pspot["shell_swp"]:
        del pspot["shell_swp"]

    if not pspot["shell_swp2"]:
        del pspot["shell_swp2"]

    pspot["projectors"] = tuple(projectors)
    pspot["string"] = string

    fix_data_types(pspot, {"beta_radius": float,
                           "r_inner": float,
                           "core_radius": float,
                           "coarse": int,
                           "medium": int,
                           "fine": int,
                           "local_channel": int})

    return pspot


def _process_pspot_report(block: TextIO) -> Dict[str, Union[float, str]]:

    accum = {"reference_electronic_structure": [],
             "pseudopotential_definition": []}

    for line in block:
        if match := REs.PSPOT_REFERENCE_STRUC_RE.match(line):
            match = match.groupdict()
            fix_data_types(match, {"occupation": float, "energy": float})
            accum["reference_electronic_structure"].append(match)
        elif match := REs.PSPOT_DEF_RE.match(line):
            match = match.groupdict()
            # Account for "loc"
            match["beta"] = int(match["beta"]) if match["beta"].isnumeric() else match["beta"]
            fix_data_types(match, {"l": int, "j": int,
                                   "e": float, "Rc": float, "norm": int})
            accum["pseudopotential_definition"].append(match)
        elif match := re.search(rf"Element: (?P<element>{REs.SPECIES_RE})\s+"
                                rf"Ionic charge: (?P<ionic_charge>{REs.FNUMBER_RE})\s+"
                                r"Level of theory: (?P<level_of_theory>[\w\d]+)", line):
            match = match.groupdict()
            match["ionic_charge"] = float(match["ionic_charge"])
            accum.update(match)

        elif match := re.search(r"Atomic Solver:\s*(?P<solver>[\w\s-]+)", line):
            accum["solver"] = normalise_string(match["solver"])

        elif match := REs.PSPOT_RE.search(line):
            accum["detail"] = _process_pspot_string(match.group(0))

        elif "Augmentation charge Rinner" in line:
            accum["augmentation_charge_rinner"] = to_type(get_numbers(line), float)

        elif "Partial core correction Rc" in line:
            accum["partial_core_correction"] = to_type(get_numbers(line), float)

    return accum


def _process_bond_analysis(block: TextIO) -> Dict[Tuple[AtomIndex, AtomIndex], Dict[str, float]]:
    accum = {((match["spec1"], int(match["ind1"])),
              (match["spec2"], int(match["ind2"]))): {"population": float(match["population"]),
                                                      "length": float(match["length"])}
             for line in block
             if (match := REs.BOND_RE.match(line))}
    return accum


def _process_orbital_populations(block: TextIO) -> Dict[str, Union[Dict[str, float],
                                                                   float,
                                                                   Tuple[float]]]:

    accum = defaultdict(dict)
    for line in block:
        if match := REs.ORBITAL_POPN_RE.match(line):
            ind = match.groupdict()
            ind = atreg_to_index(ind)
            accum[ind][match["orb"]] = to_type(match["charge"], float)
        elif match := re.match(rf"\s*Total:\s*{labelled_floats(('charge',))}", line):
            accum["total"] = float(match["charge"])
        elif "total projected" in line:
            accum["total_projected"] = to_type(get_numbers(line), float)

    return accum


def _process_dftd(block: TextIO) -> Dict[str, Union[Dict[str, float], float]]:
    dftd = {"species": {}}

    for line in block:
        if len(match := line.split(":")) == 2:
            key, val = match
            val = normalise_string(val)
            if "Parameter" in key:
                val = to_type(get_numbers(val)[0], float)
            dftd[normalise_string(key).lower()] = val

        elif match := re.match(rf"\s*x\s*(?P<spec>{REs.ATOM_NAME_RE})\s*" +
                               labelled_floats(('C6', 'R0')), line):
            dftd["species"][match["spec"]] = {"C6": float(match["C6"]),
                                              "R0": float(match["R0"])}

    return dftd


def _process_occupancies(block: TextIO) -> Dict[str, Union[int, float]]:
    label = ("band", "eigenvalue", "occupancy")

    accum = [dict(zip(label, numbers)) for line in block if (numbers := get_numbers(line))]
    for elem in accum:
        fix_data_types(elem, {"band": int,
                              "eigenvalue": float,
                              "occupancy": float})
    return accum


def _process_wvfn_line_min(block: TextIO) -> Dict[str, Tuple[float]]:
    accum = {}
    for line in block:
        if "initial" in line:
            accum["init_energy"], accum["init_de_dstep"] = to_type(get_numbers(line), float)
        elif line.strip().startswith("| step"):
            accum["steps"] = to_type(get_numbers(line), float)
        elif line.strip().startswith("| gain"):
            accum["gain"] = to_type(get_numbers(line), float)

    return accum


def _process_autosolvation(block: TextIO) -> Dict[str, float]:

    accum = {}
    for line in block:
        if len(match := line.split("=")) > 1:
            key = normalise_string(match[0].strip("-( "))
            val = to_type(get_numbers(line)[0], float)
            accum[key] = val

    return accum


# def _process_phonon(block: TextIO):
#     ...

def _process_dipole(block: TextIO) -> Dict[str, Union[ThreeVector, float]]:

    accum = {}

    for line in block:
        if match := re.search(r"Total\s*(?P<type>\w+)", line):
            accum[f"total_{match['type']}"] = float(get_numbers(line)[0])

        elif "Centre" in line:
            key = "centre_electronic" if "elec" in line else "centre_positive"
            accum[key] = to_type(get_numbers(next(block)), float)

        elif "Magnitude" in line:
            accum["dipole_magnitude"] = to_type(get_numbers(line)[0], float)

        elif "Direction" in line:
            accum["dipole_direction"] = to_type(get_numbers(line), float)

    return accum


def _process_pair_params(block_in: TextIO) -> Dict[Union[str, Tuple[str]], float]:

    accum = {}
    for line in block_in:
        # Two-body
        if block := get_block(line, block_in, "Two Body", r"^\w*\s*\*+\s*$"):
            for blk_line in block:
                if REs.PAIR_POT_RES['two_body_spec'].search(blk_line):
                    match = REs.PAIR_POT_RES['two_body_spec'].finditer(blk_line)
                    labels = tuple(mch.groups() for mch in match)

                elif match := REs.PAIR_POT_RES['two_body_val'].match(blk_line):
                    tag, typ, lab = match.group("tag", "type", "label")
                    if tag:
                        typ = f"{tag}_{typ}"
                    if typ not in accum:
                        accum[typ] = {}
                    if lab not in accum[typ]:
                        accum[typ][lab] = {}

                    accum[typ][lab].update(zip(labels,
                                               to_type(match["params"].split(),
                                                       float)))

                elif match := REs.PAIR_POT_RES['two_body_one_spec'].match(blk_line):
                    labels = (match["spec"],)

        # Three-body
        elif block := get_block(line, block_in, "Three Body", r"^\s*\*+\s*$"):
            for blk_line in block:
                if match := REs.PAIR_POT_RES['three_body_spec'].match(blk_line):
                    labels = (tuple(match["spec"].split()),)

                elif match := REs.PAIR_POT_RES["three_body_val"].match(blk_line):
                    tag, typ, lab = match.group("tag", "type", "label")

                    if tag:
                        typ = f"{tag}_{typ}"
                    if typ not in accum:
                        accum[typ] = {}
                    if lab not in accum[typ]:
                        accum[typ][lab] = {}

                    accum[typ][lab].update(zip(labels,
                                               to_type(match["params"].split(),
                                                       float)))

        # Globals
        elif match := REs.PAIR_POT_RES["three_body_val"].match(line):
            tag, typ, lab = match.group("tag", "type", "label")

            if tag:
                typ = f"{tag}_{typ}"
            if typ not in accum:
                accum[typ] = {}

            accum[typ][lab] = to_type(match["params"], float)

    return accum


def _process_geom_table(block: TextIO) -> Dict[str, Union[bool, float]]:

    accum = {}
    for line in block:
        if match := REs.GEOMOPT_MIN_TABLE_RE.match(line):
            match = match.groupdict()
            fix_data_types(match, {key: float for key in ('lambda', 'Fdelta', 'enthalpy')})

            key = normalise_string(match["step"])
            del match["step"]
            accum[key] = match

        elif match := REs.GEOMOPT_TABLE_RE.match(line):
            match = match.groupdict()
            fix_data_types(match, {key: float for key in ('value', 'tolerance')})

            match["converged"] = match["converged"] == "Yes"

            key = normalise_string(match["parameter"])
            del match["parameter"]
            accum[key] = match

    return accum


def _process_elastic_properties(block: TextIO) -> Dict[str, Tuple[float]]:
    accum = {}

    for line in block:
        if "::" in line:
            key = line.split("::")[0]
            val = to_type(get_numbers(line), float)

            if len(val) == 1:
                val = val[0]

            accum[normalise_string(key)] = val
        elif blk := get_block(line, block, "Speed of Sound", REs.EMPTY):

            accum["Speed of Sound"] = [to_type(numbers, float)
                                       for blk_line in blk
                                       if (numbers := get_numbers(blk_line))]

    return accum
