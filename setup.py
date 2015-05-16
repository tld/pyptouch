#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

import pyptouch

class Tox(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

setup(
    name='pyptouch',
    version=pyptouch.__version__,
    description='Driver for Brothers P-Touch series of label printers.',
    url='https://github.com/tld/pyptouch',
    license="BSD",
    author="Terje Elde",
    author_email='terje@elde.net',
    long_description=readme + '\n\n' + history,
    packages=[
        'pyptouch'
    ],
    package_dir={'pyptouch': 'pyptouch'},
    scripts=['bin/png2ptouch'],
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='pyptouch',
    cmdclass={'test': Tox},
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Topic :: Office/Business',
        'Topic :: Printing',
        'Topic :: Text Processing',
        'Topic :: Utilities'
    ],
    extras_require={
        'png':      ['Pillow>=2.6']
    },
    #test_suite='tests',
    tests_require=['nose']
)
