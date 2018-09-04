#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2018 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from setuptools import setup

setup(
    name='gdscene',
    version='0.0.1',
    description='Simple library to make it easier to generate Godot scene files programmatically',
    author='Taylor C. Richberger <taywee@gmx.com>',
    author_email='taywee@gmx.com',
    url='https://github.com/Taywee/gdscene',
    license='GPL3',
    entry_points={
        'console_scripts': [
            'tilemap = gdscene.__main__:tilemap',
            ]
        },
    packages=[
        'gdscene',
        ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        ],
)
