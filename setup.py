'''
Script to install shortestpath as a command line application
'''

from setuptools import setup

setup(name = 'shortestpath',
      version = '1.0',
      packages = ['shortestpath'],
      entry_points = {'console_scripts': [ 'shortestpath  =shortestpath.__main__:main']})

