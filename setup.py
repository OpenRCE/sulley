#!/usr/bin/env python

from setuptools import setup

setup(
    name='sulley',
    version=0.1,
    description='A pure-python fully automated'
                'and unattended fuzzing framework.',
    author='OpenRCE',
    packages=['sulley', 'sulley.legos', 'sulley.pgraph', 'sulley.utils'],
    install_requires=[
        'pydot'
    ]
)
