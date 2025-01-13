# soti-mobicontrol-python

## Introduction 
This is Python library wrapper the SOTI MobiControl REST API to manage devices, profiles, and packages. 

### Project structure
https://matt.sh/python-project-structure-2024


### Setup the environment
Intall the Python slected version using pyenv using the following commands:
```bash

pyenv install 3.13.0



pyenv shell 3.13.0

curl -sSL https://install.python-poetry.org | python3

poetry init

poetry install
```

### Activate the environment
```bash
poetry env use ~/.pyenv/versions/3.13.0/bin/python


```

### Install the dependencies
samples:
```bash

poetry add anyio
poetry add httpx

```


### Build the package locally
```bash
poetry build
```

### Test the package
Make sure the the tests are found

```bash
pytest --collect-only
```


# Manually build and publish the package to https://test.pypi.org/
Inclenment the version in the pyproject.toml file

## Setup 
Make sure you have the API token from the https://test.pypi.org/ and configure the repository and the token in the poetry
```bash
poetry config repositories.test-pypi https://test.pypi.org/legacy/
poetry config pypi-token.test-pypi <your-api-token>

```


Build the package and publish it to the test.pypi.org
```bash
poetry build
poetry publish --repository test-pypi
```