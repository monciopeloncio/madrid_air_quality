# Madrid Air Quality Package

## Instructions to create a build and upload the package

```bash
# Create a new build using the setup.py configuration
python3 setup.py sdist bdist_wheel

# Upload to pipy
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```