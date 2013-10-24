#!/usr/bin/env python
from distutils.core import setup

long_description = None

setup(
    name='backports.statistics',
    version='0.1',
    packages=['backports.statistics'],
    namespace_packages=['backports'],
    author="Steven D'Aprano",
    author_email='steve@pearwood.info',
    maintainer='Christian Heimes',
    maintainer_email='christian@python.org',
    url='https://bitbucket.org/tiran/backports.statistics',
    keywords='statistics',
    #platforms='',
    license='PSFL',
    description='statistics backport 2.6 - 3.3',
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
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
    ],
)

