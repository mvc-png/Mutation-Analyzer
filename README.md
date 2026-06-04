### Protein Mutation Analysis Toolkit

A Python-based tool for analyzing amino acid substitutions between a wild-type and mutant protein sequence. The script identifies mutations, classifies them according to biochemical properties, assigns severity scores, and visualizes secondary structure differences using a bar chart.
The sequences used for this project are Hemoglobin sequences, P69892 - HBG2_HUMAN (wild type) and 69891 - HBG1_HUMA (mutant).

---

## Features

- Detects amino acid substitutions between two protein sequences
- Classifies mutations as:
  1. Conservative
  2. Non-conservative
  3. Charge Reversal
  4. Possible Helix Disruption (Proline substitutions)
- Assigns mutation severity scores
- Counts total mutations
- Generates comparison plots using Matplotlib

---

## Mutation Classification Rules

### Conservative Mutations
Substitutions within the same biochemical group:

| Group | Amino Acids |
|---------|---------|
| Hydrophobic | A, V, I, L, M, F, W, Y |
| Polar | S, T, N, Q |
| Positive | K, R, H |
| Negative | D, E |

Examples:
- L → I
- D → E
- K → R

**Severity Score:** 1

---

### Charge Reversal Mutations

Examples:
- D → K
- E → R
- K → D

**Severity Score:** 2

---

### Non-Conservative Mutations

Substitutions between different amino acid groups.

Examples:
- A → S
- V → Q

**Severity Score:** 2

---

### Possible Helix Disruption

Mutations introducing Proline may disrupt alpha-helices due to its rigid, cyclic structure.

Examples:
- A → P
- L → P

**Severity Score:** 3

---

## Example Output

```text
Mutations observed at positions:

Position 83 : I -> T | Non-conservative | Severity Score: 2

Total mutations: 1
```

---

## Secondary Structure Comparison

The script compares predicted secondary structure composition between wild-type and mutant proteins.

Structure categories:
- Alpha Helix
- Beta Sheet
- Turn
These values were computed using https://www.biogem.org/.

Example values:

```python
wild = [57.5, 35.8, 6.7]
mutant = [45.2, 42.1, 12.7]
```

The script generates a side-by-side bar chart to visualize structural differences.

---

## Requirements

Install the required packages:

```bash
pip install matplotlib numpy
```

---


## Example Dataset

### Wild-Type Sequence

```text
MGHFTEEDKATITSLWGKVNVEDAGGETLGRLLVVYPWTQRFFDSFGNLSSASAIMGNPKVKAHGKKVLTSLGDAIKHLDDLKGTFAQLSELHCDKLHVDPENFKLLGNVLVTVLAIHFGKEFTPEVQASWQKMVTGVASALSSRYH
```

### Mutant Sequence

```text
MGHFTEEDKATITSLWGKVNVEDAGGETLGRLLVVYPWTQRFFDSFGNLSSASAIMGNPKVKAHGKKVLTSLGDATKHLDDLKGTFAQLSELHCDKLHVDPENFKLLGNVLVTVLAIHFGKEFTPEVQASWQKMVTAVASALSSRYH
```

---

## Future Improvements

- Read sequences directly from FASTA files
- Support multiple sequence alignment
- Integrate BLOSUM62 substitution scoring
- Predict mutation effects on protein stability
- Export mutation reports to CSV
- Generate mutation heatmaps
- Add PyMOL structure comparison support
- Integrate AlphaFold/ColabFold structure prediction workflows

---

