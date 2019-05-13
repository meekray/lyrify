"""
Setup partycity as a python package.
Installs all dependencies and installs lyrify as a python package.
"""

from setuptools import setup

setup(
    name='lyrify',
    version='0.1.0',
    include_package_data=True,
    install_requires=[
        'nltk',
        'bs4',
        'pandas',
        'requests'
    ],
)
