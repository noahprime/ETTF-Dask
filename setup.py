import re
from setuptools import setup, find_packages


def readme():
    """Return the contents of the project README file."""

    with open('README.md') as f:
        return f.read()

setup(
    name='ETTF Dask',
    version='0.0.0',
    packages=find_packages(),
    url='https://github.com/noahprime/ETTF-Dask',
    license='BSD-2-Clause',
    author='Noah Prime',
    author_email='noah.prime@pnnl.gov',
    description='',
    long_description=readme(),
    long_description_content_type="text/markdown",
    python_requires='>=3.6.*, <4',
    include_package_data=True,
    install_requires=[
        "dask",
        "matplotlib!=3.6.1,>=3.1",
        "numpy",
        "netCDF4",
        "pandas",
        "PyYAML",
        "seaborn",
        "xarray"
    ],
    extras_require={
        'dev': [
            "plotly",
            "xesmf"
        ]
    }
)
