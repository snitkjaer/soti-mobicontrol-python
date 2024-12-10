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