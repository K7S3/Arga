# Arga

Linear Regression Model to predict revenue.

## Project Structure

- `data/` - Contains raw and predicted data.
- `notebooks/` - Contains code to do both data analysis and predicting revenue with linear regression.
- `scripts/` - Contains a script to convert xl files to csv
- `tests/` - Contains unit test for data processing.

## Setup

- Create a virtual environment(python 3.10) and install dependencies with these commands:

```sh
# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

# Install dependencies
pip install -r requirements.txt 

```

## Running Tests

- Test can be run with the following command

```
python -m unittest tests/test_data.py
```



