#!/usr/bin/env python

from setuptools import setup

setup(name='mpl_styles',
      version='0.1.0.dev',
      description='Pre-defined Matplotlib styles',
      author='Thomas Robitaille, Joao Alves',
      author_email='thomas.robitaille@gmail.com',
      packages=['mpl_styles'],
      provides=['mpl_styles'],
      requires=['brewer2mpl'],
      keywords=['Scientific/Engineering'],
     )
