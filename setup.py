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

setup(name='napoleon',
      version='0.15',
      description='A python package for making plotly simple to get up and running',
      url='http://github.com/mitchelllisle/napoleon',
      author='Mitchell Lisle',
      author_email='lislemitchell@gmail.com',
      license='MIT',
      packages=['napoleon'],
      zip_safe=False,
      python_requires='>=3'
)
