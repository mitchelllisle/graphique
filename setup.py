#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:copyright: (c) 2017 by Lev Lazinskiy
:license: MIT, see LICENSE for more details.
"""
import os
import sys

from setuptools import setup
from setuptools.command.install import install

# circleci.py version
VERSION = "1.1.1"

def readme():
    """print long description"""
    with open('README.rst') as f:
        return f.read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, VERSION
            )
            sys.exit(info)

setup(name='graphique',
      version=VERSION,
      description='A python package for making plotly simple to get up and running',
      long_description=readme(),
      url='http://github.com/mitchelllisle/graphique',
      author='Mitchell Lisle',
      author_email='lislemitchell@gmail.com',
      license='MIT',
      packages=['graphique'],
      zip_safe=False,
      python_requires='>=3',
      cmdclass={
        'verify': VerifyVersionCommand,
        }
)
