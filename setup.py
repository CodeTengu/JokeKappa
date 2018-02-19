#!/usr/bin/env python
# coding: utf-8

import os
import sys

from setuptools import find_packages
from setuptools import setup


def get_version():
    code = None
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'jokekappa',
        '__init__.py',
    )
    with open(path) as f:
        for line in f:
            if line.startswith('__version__'):
                code = line[len('__version__ = '):]
                break
    return eval(code)


if sys.argv[-1] == 'wheel':
    os.system('rm -rf dist/*')
    os.system('pip install wheel')
    os.system('python setup.py bdist_wheel')
    sys.exit(0)

if sys.argv[-1] == 'publish':
    os.system('python setup.py wheel')
    os.system('pip install twine')
    os.system('twine upload dist/*')
    sys.exit(0)

long_description = open('README.rst').read()

requirements_lines = [line.strip() for line in open('requirements.txt').readlines()]
install_requires = list(filter(None, requirements_lines))

setup(
    name='jokekappa',
    version=get_version(),
    url='https://github.com/CodeTengu/JokeKappa',
    description='A library for delivering one-line programming jokes.',
    long_description=long_description,
    keywords='jokes programming-jokes',
    author='Vinta Chen',
    author_email='vinta.chen@gmail.com',
    license='MIT',
    install_requires=install_requires,
    scripts=['scripts/jokekappa', ],
    packages=find_packages(exclude=('tests', )),
    include_package_data=True,
    test_suite='tests',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ),
)
