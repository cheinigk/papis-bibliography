#!/usr/bin/env python3

from setuptools import setup

with open('README.md') as fd:
    long_description = fd.read()

setup(
    name='papis-bibliography',
    version='0.0.1',
    author='Christian Heinigk',
    author_email='christian.heinigk@nld.rwth-aachen.de',
    license='MIT',
    url='https://github.com/cheinigk/papis-bibliography',
    install_requires=[
        "papis==0.12",
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
    description='Bibliography exporter for papis',
    long_description=long_description,
    keywords=[
        'papis', 'cli', 'biliography', 'exporter'
    ],
    entry_points={
        'papis.exporter': [
            'bibliography=papis_bibliography.bibliography:exporter',
        ]
    },
    packages=['papis_bibliography'],
    platforms=['linux', 'osx'],
)
