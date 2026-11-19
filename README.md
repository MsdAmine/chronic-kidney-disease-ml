# Chronic Kidney Disease Prediction Using Machine Learning

## Project Overview

An academic Data Mining project developed by two fifth-year software engineering
students, within the theme of Medicine, Health and Well-being. The task is
supervised binary classification of Chronic Kidney Disease (CKD) versus Not CKD
using the UCI Chronic Kidney Disease dataset.

## Project Objectives

- Explore the dataset through exploratory data analysis (EDA).
- Identify and compare appropriate preprocessing techniques.
- Compare Logistic Regression, K-Nearest Neighbors (KNN), Decision Tree and
  Random Forest classifiers under equivalent experimental conditions.
- Evaluate models and iteratively improve the methodology.
- Investigate feature importance and interpret the classification results.

## Dataset

The [official UCI dataset page and feature descriptions](https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease)
describe 400 records, 24 input features and one target, `class`. The expected
target categories are `ckd` and `notckd`. The hosted CSV uses `wbcc` and `rbcc`
for white and red blood cell counts.

- [Official CSV source](https://archive.ics.uci.edu/static/public/336/data.csv)
- [Official metadata, feature descriptions and units](https://archive.ics.uci.edu/api/dataset?id=336)
- Creators: L. Rubini, P. Soundarapandian and P. Eswaran.
- Dataset license: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

Citation: Rubini, L., Soundarapandian, P., & Eswaran, P. (2015).
*Chronic Kidney Disease* [Dataset]. UCI Machine Learning Repository.
DOI: [10.24432/C5G020](https://doi.org/10.24432/C5G020).

Dataset reuse must retain appropriate attribution, link to the license and
identify any modifications. The downloader preserves the original response bytes
unchanged. Raw data is stored locally and excluded from Git.

Verified local retrieval:

| Property | Value |
| --- | --- |
| Retrieval date (UTC) | 2026-11-19 |
| File size | 45,092 bytes |
| Local path | `data/raw/chronic_kidney_disease.csv` |

SHA-256:

```text
0EEEA8D17F5AD8792D854999D6DDF1602EC4E116616F6CCDFDAEF0BA8109E694
```

Read-only loading diagnostics found the raw target labels `ckd`, `ckd\t` and
`notckd`; `\t` represents a tab. Missing values in the CSV are represented by
literal `NaN`, which Pandas recognizes by default. The tests strip target
whitespace only for temporary comparisons and leave the raw file unchanged.

## Technologies

- Python 3.11.9.
- NumPy and Pandas for numerical and tabular data.
- Matplotlib and Seaborn for planned visualizations.
- Scikit-learn for planned preprocessing, training and evaluation.
- JupyterLab for planned notebook experiments.
- Python standard library for dataset retrieval and `unittest` validation.
- Git and GitHub for version control and collaboration.

Exact direct and transitive package versions are recorded in `requirements.txt`
using `pip freeze`. Direct dependencies are the six selected libraries;
transitive dependencies are packages those libraries require.

## Project Structure

The current layout is shown below. The CSV and `.venv/` are local, ignored
artifacts. Git metadata, bytecode caches and local configuration are omitted.

```text
chronic-kidney-disease-ml/
|-- data/
|   |-- raw/
|   |   |-- .gitkeep
|   |   `-- chronic_kidney_disease.csv
|   `-- processed/
|       `-- .gitkeep
|-- notebooks/
|   `-- .gitkeep
|-- src/
|   `-- download_data.py
|-- tests/
|   `-- test_dataset_loading.py
|-- models/
|   `-- .gitkeep
|-- reports/
|   `-- figures/
|       `-- .gitkeep
|-- .venv/
|-- .gitignore
|-- requirements.txt
`-- README.md
```

| Directory | Purpose |
| --- | --- |
| `data/` | Raw and generated project data. |
| `data/raw/` | Original, unchanged dataset files. |
| `data/processed/` | Generated and transformed datasets. |
| `notebooks/` | Planned EDA and machine learning experiments. |
| `src/` | Reusable Python code and the dataset downloader. |
| `tests/` | Automated loading and validation checks. |
| `models/` | Generated trained models. |
| `reports/` | Documentation and experimental results. |
| `reports/figures/` | Exported visualizations. |
| `.venv/` | Local Python virtual environment. |

Empty directories are retained with `.gitkeep` files. Raw data, generated
datasets, trained models, virtual environments, local environment configuration
and IDE settings are excluded from Git. `.env.example` remains trackable if
introduced later; source code, notebooks, reports and figures remain trackable.

## Getting Started

Install Python 3.11.9 and Git. Run the following commands in Windows PowerShell.

Clone the repository and enter its root directory:

```powershell
git clone https://github.com/MsdAmine/chronic-kidney-disease-ml.git
cd chronic-kidney-disease-ml
```

Verify the Python version, then create and activate a virtual environment. Create
`.venv` only if it does not already exist.

```powershell
python -c "import sys; print(sys.version); assert sys.version_info[:3] == (3, 11, 9)"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Verify the environment's interpreter. The output should identify `.venv` and
Python 3.11.9; the assertion confirms that Python is running inside a virtual
environment.

```powershell
.\.venv\Scripts\python.exe -c "import sys; print(sys.executable); print(sys.version)"
.\.venv\Scripts\python.exe -c "import sys; assert sys.prefix != sys.base_prefix"
```

Install the frozen dependencies and check their consistency:

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip check
```

All pip commands explicitly use the virtual environment's Python executable.
Installation from this manifest was successfully reproduced in a fresh Python
3.11.9 environment on Windows, with matching frozen versions, successful imports
of all six direct dependencies and no broken requirements. Other platforms have
not been verified.

## Dataset Retrieval

From the repository root, run:

```powershell
.\.venv\Scripts\python.exe src/download_data.py
```

The standard-library downloader saves the official CSV to
`data/raw/chronic_kidney_disease.csv`. It uses a 30-second network timeout, rejects
empty or detectably incomplete responses, and stages complete binary data before
publishing the final file. Staging and publication use the same filesystem;
publication requires hard-link support.

An existing destination is preserved, including when another process creates it
during retrieval. Repeated execution skips the existing file. Successful or
skipped downloads exit with status `0`; failures print a message and exit with
status `1`. Internet access is required for the initial download.

Check the local checksum against the recorded value above:

```powershell
Get-FileHash -LiteralPath data/raw/chronic_kidney_disease.csv -Algorithm SHA256
```

## Dataset Validation

After retrieving the dataset, run the offline validation suite:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

The seven tests verify:

1. Availability of a nonempty local dataset file.
2. Successful CSV loading as a Pandas DataFrame.
3. Exactly 400 rows and 25 columns.
4. Exact column names and order against the independently verified UCI schema.
5. Presence of the `class` target column.
6. Absence of missing, empty or whitespace-only target labels.
7. Exactly `ckd` and `notckd` after temporary target-whitespace normalization.

If the dataset is missing, class setup fails with the downloader command.
Verification on Python 3.11.9 completed with all seven tests passing. The
downloader's repeat invocation preserved file size, last-write timestamp and
SHA-256; the dataset checksum also remained unchanged after loading tests.

## Project Methodology

The planned Data Mining workflow is:

1. **Dataset understanding:** review provenance, feature meanings, types, missing
   values and inconsistencies before choosing transformations.
2. **Exploratory data analysis:** examine distributions, relationships and
   clinically plausible extreme values without automatically removing them.
3. **Preprocessing and comparison:** justify and compare imputation, encoding and
   scaling. Fit learned transformations only on training data, independently
   within each cross-validation fold, using pipelines where appropriate.
4. **Model training and comparison:** compare the four planned classifiers using
   a consistent stratified split, documented random seeds and shared
   cross-validation splits. Reserve the final test set for final evaluation.
5. **Evaluation and iterative improvement:** assess accuracy, precision, recall,
   F1-score, confusion matrices and ROC-AUC where appropriate. Pay particular
   attention to CKD recall and false negatives, interpret feature contributions,
   and improve methods without using the final test set for model selection.

## Current Project Status

Completed setup includes the directory structure, exclusion rules, frozen Python
dependencies with reproducibility checks, safe UCI dataset retrieval and seven
passing dataset loading tests.

EDA, preprocessing comparisons, model training, tuning, feature-importance
analysis and model evaluation are planned. No experiment notebooks, trained
models or predictive performance results have been produced.

## Limitations

This project is educational and uses a small dataset of 400 records containing
missing values and observed target whitespace. It has no clinical validation.
Dataset validation checks establish loading and schema consistency; they do not
establish diagnostic reliability. Any future model scores on this dataset must
be interpreted cautiously and cannot establish suitability for clinical use.
