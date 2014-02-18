#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python packaging."""
from setuptools import setup

name = 'test'
description = 'test'
version = ""
readme = ""
requirements = ['pytz==2013d']
entry_points = {}


if __name__ == '__main__':  # ``import setup`` doesn't trigger setup().
    setup(name=name,
          version=version,
          description=description,
          long_description=readme,
          author='Me',
          author_email='boris.feld@novapost.net',
          url='https://github.com/Lothiraldan/test_pyz_dep',
          install_requires=requirements,
          entry_points=entry_points)
