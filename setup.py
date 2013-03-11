#!/bin/env python
# -*- coding: utf8 -*-
from setuptools import setup, find_packages

try:
    import multiprocessing, logging
except ImportError:
    pass

version = '0.0.1'

setup(name='pythong',
      version=version,
      description="Set up a minimal, yet comfortable structure \
                    for a Python project",
      classifiers=[
          "Development Status :: Planning",
          "Intended Audience :: Developers",
          "License :: MIT",
          "Programming Language :: Python :: 2",
          "Topic :: Software Development",
          "Topic :: Utilities",
      ],
      keywords='python development project bootstrap',
      author='David Gay',
      author_email='oddshocks@gmail.com',
      url='http://github.com/oddshocks/pythong',
      license='GPLv3+',
      packages=find_packages(exclude=['ez_setup', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=['nose', 'mock', 'six', 'jinja2'],
      entry_points="""
      [console_scripts]
      pythong = pythong:create_project
      """)
