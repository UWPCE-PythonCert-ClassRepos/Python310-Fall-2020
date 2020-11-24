#!/usr/bin/env python

"""
package setup script for mailroom
"""

from pathlib import Path
from setuptools import setup


def get_version(package):
    """
    Reads the version string from the package __init__ and returns it
    """
    with open(Path(package) / "__init__.py") as init_file:
        for line in init_file:
            parts = line.strip().partition("=")
            if parts[0].strip() == "__version__":
                return parts[2].strip().strip("'").strip('"')
    return None


setup(name='mailroom',
      version=get_version(),
      packages=['mailroom', 'mailroom/tests'],
      scripts=['scripts/mailroom.py'],
      author='An Awsome Coder',
      author_email='aac@example.com',
      url='http://mailroom.example.org/',
      description='A system for managing donation for a non-profit',
      long_description=open('README.rst').read(),
      )
