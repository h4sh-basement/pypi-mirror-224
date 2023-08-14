# Microservice Shared Package

The Microservice Shared Package is a collection of utility functions, models, serializers, and other components shared across microservices in your project. This package is designed to simplify the development and maintenance of your microservices architecture.

## Installation

To install the Microservice Shared Package, use pip:


## Setup Deployment Environment

Setup PYPI API token for upload your package to PyPI

```bash
echo %homepath%       # Execute this command into command prompt it will show your user account location ex: C:\Users\johndoe
```

Create .pypirc file in profile main directory and open that file, add the following lines:

```bash
[pypi]
username = __token__
password = YOUR_API_TOKEN   # Replace YOUR_API_TOKEN with the value of your API token.
```

## Deployment

To deploy the Microservice Shared Package, use `twine`:

```bash
python -m build                     # build distribution packages new way
python setup.py sdist bdist_wheel   # build distribution packages

twine upload --verbose dist/*       # Upload distribution packages with addition details
twine upload dist/*                 # Upload distribution packages
```
## Debug

To debug the Microservice Shared Package, use `python`:

```python
$ cd path/to/microservice_shared
$ python
Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from microservice_shared.utils import to_uppercase
>>> print(to_uppercase("message"))
MESSAGE
>>> exit()
```

## Local Installation

Install the Microservice Shared Package in local:

```bash
#Install another microservice inside
cd path/to/microservice_shared
python -m build # Here you will get whl file: microservice_shared-0.2.0-py2.py3-none-any.whl

cd path/to/microservice_authentication
poetry add ../microservice_shared/dist/microservice_shared-0.2.0-py2.py3-none-any.whl

# Only install current project not global (Outdated)
pip install -e .
pip uninstall microservice_shared -y
```

## Setup Commands

These are the important Python setup commands that you can use to build, install, test, register, and upload your Python package:

```python
python setup.py build       # Builds your Python package.

python setup.py install     #  Installs your Python package into your Python environment.

python setup.py test        #  Runs the tests for your Python package.

python setup.py register    # Registers your Python package with PyPI.

#  Creates a source distribution of your Python package. This command will create a file called dist/<package_name>-<version>.tar.gz that contains your package source code.
python setup.py sdist

#  Creates a wheel distribution of your Python package. This command will create a file called dist/<package_name>-<version>-py3-none-any.whl that contains your packages built files in a wheel format.
python setup.py bdist_wheel

```

## Twine Commands

Here are some important twine commands that you can use to upload your Python package to PyPI:

```python
# This command will take all of the files in the dist directory and upload them to PyPI.

twine upload dist/*

#  Shows the progress of the upload. This command is useful for troubleshooting if you are having problems uploading your package.

twine upload --verbose dist/*

# This command checks your Python package for any errors before you upload it to PyPI. This command is useful for making sure that your package is properly formatted and that it does not contain any errors.

twine check dist/*

# This command uploads your Python package to the test PyPI server. This server is a mirror of the production PyPI server, but it is not used for production releases. This command is useful for testing your upload process before you upload your package to the production PyPI server.

twine upload --repository testpypi dist/*

```

## Usage

### Using Utility Functions

You can use the provided utility functions in your microservices. For example, to convert a string to uppercase:

```python
from microservice_shared.<utils-name> import <method-name>
```
