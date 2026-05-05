# Jenkins Python Sample

This repository contains a small Python data-processing example with a Jenkins pipeline.

## Structure

- `src/static_data.py`: static sample customer data
- `src/data_loader.py`: loads the static data into a pandas DataFrame
- `src/preprocessing.py`: applies simple preprocessing rules
- `src/test_preprocessing.py`: basic unit tests for loading and preprocessing
- `requirements.txt`: Python dependencies
- `Jenkinsfile`: Jenkins pipeline to install dependencies, compile `src`, and run tests

## Run locally

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run tests:

```powershell
python -m unittest discover -s src -p "test_*.py" -v
```

## Jenkins

The pipeline is scoped to this folder only. It:

- installs packages from `requirements.txt`
- compiles Python files in `src`
- runs the unit tests in `src`
