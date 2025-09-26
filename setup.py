#!/usr/bin/env python
from setuptools import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_kwargs = generate_distutils_setup()
setup_kwargs['packages'] = ['cuzk_tools']
setup_kwargs['package_dir'] = {'': 'src'}

setup(**setup_kwargs)
