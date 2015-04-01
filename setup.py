#!/usr/bin/env python
from setuptools import setup

long_description = """
Backport of http://docs.python.org/3.4/library/statistics.htm
"""

setup(
    name='backports.statistics',
    version='0.1.0',
    packages=['backports.statistics'],
    namespace_packages=['backports'],
    author="Steven D'Aprano",
    author_email='steve@pearwood.info',
    maintainer='Thomas Grainger',
    maintainer_email='backports.statistics@graingert.co.uk',
    url='https://github.com/graingert/backports.statistics',
    keywords='statistics',
    platforms='platform independent',
    license='PSFL',
    description='statistics backport 2.6 - 3.3',
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Python Software Foundation License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
)
