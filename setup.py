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

setup(name='graphique',
      version='0.14',
      description='A python package for making plotly simple to get up and running',
      url='http://github.com/mitchelllisle/graphique',
      author='Mitchell Lisle',
      author_email='lislemitchell@gmail.com',
      license='MIT',
      packages=['graphique'],
      zip_safe=False,
      python_requires='>=3'
)
