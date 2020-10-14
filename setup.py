from os import name
from callonce._version import __version__
from setuptools import setup, find_packages


setup(
    name='callonce',
    version=__version__,
    description='make a function callable for once or N times',
    packages=find_packages(exclude=['tests'])
)
