"""
Setup partycity as a python package.
Installs all dependencies and installs lyrify as a python package.
"""

from setuptools import setup

# pip install -e .

setup(name='lyrify',
      packages=['lyrify'],
      version='0.1.0',
      install_requires=[
        'nltk',
        'bs4',
        'pandas',
        'requests',
        'flask',
        'pprint',
        'pymongo'
      ],
      entry_points={
          'console_scripts': [
              'lyrify=lyrify.__main__:main'
          ]
      },
    )
