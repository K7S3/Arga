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

## Code Standards

Black: The project uses Black for code formatting. Black is a Python code formatter that enforces a consistent coding style. It is configured to check code formatting as part of the continuous integration pipeline.

Flake8: We use Flake8 for linting the Python code. Flake8 is a tool that checks for style issues as well as programming errors. It's configured to enforce a maximum line length of 88 characters.

Unit Testing: The project uses Python's built-in unittest module for unit testing. All tests are located in the tests/ directory and can be run with the command python -m unittest tests/test_data.py.

Continuous Integration: The project uses GitHub Actions for continuous integration. The configuration is located in .github/workflows/tests.yml. The CI pipeline checks out the code, sets up Python, installs dependencies, checks code formatting with Black, lints the code with Flake8, and runs the unit tests.

Jupyter Notebooks: The Jupyter notebooks in the notebooks/ directory follow best practices for reproducible research. This includes clear documentation of each step, keeping cells small and focused, and including both the input and output in the saved notebook.

Requirements Management: All Python dependencies are listed in the requirements.txt file. This makes it easy to set up a consistent environment for running the code.

