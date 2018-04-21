
# coding: utf-8

"""
Setup script for installing fastai
"""

##########################################################################
## Imports
##########################################################################

#from distutils.core import setup
from setuptools import setup


##########################################################################
## Setup
##########################################################################

setup(
    name = "fastai_gans",
    packages = ['gans', 'gans/data', 'gans/models', 'gans/options', 'gans/util'],
    version = 0.1 ,
    description = "CycleGAN and Pix2Pix",
    author = "",
    author_email = "",
    license = "Apache License 2.0",
    install_requires =
     ['visdom', 'dominator'],
    keywords = ['deeplearning', 'pytorch', 'machinelearning'],
    classifiers = ['Development Status :: 3 - Alpha', 'Programming Language :: Python', 'Programming Language :: Python :: 3.6']
)

