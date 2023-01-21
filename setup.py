#!/usr/bin/env python

from distutils.core import setup

setup(name='Fairvasc Utilities',
      version='0.1',
      description='Fairvasc Utilities',
      author='Fairvasc',
      author_email='',
      url='',
      packages=[
            'fairvasc_util',
      ],
      install_requires=[
            'pandas',
            'jupyter',
            'sparql_dataframe',
      ],
      )
