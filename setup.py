import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Madrid Air Quality",
    version="0.0.1",
    author="Ramón Pintado",
    author_email="ramonpintado91@gmail.com",
    description="Madrid Air Quality Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/monciopeloncio/madrid_air_quality",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
