#!/usr/bin/env python
# coding: utf-8

from setuptools import find_packages
from setuptools import setup


setup(
    name='salada',
    version='0.0.1',
    description='A server and tools for K-best word completion.',
    url='https://github.com/mitsuse/salada',
    author='Tomoya Kose',
    author_email='tomoya@mitsuse.jp',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='language word completion server',
    packages=find_packages(
        exclude=[
        ]
    ),
    entry_points={
        'console_scripts': [
            'salada = salada.command:main',
        ],
    },
)
