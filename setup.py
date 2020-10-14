from os import name

from setuptools import find_packages, setup

from callonce._version import __version__

setup(
    name='callonce',
    version=__version__,
    description='make a function callable for once or N times',
    packages=find_packages(exclude=['tests'])
)
