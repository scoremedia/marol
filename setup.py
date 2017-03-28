# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='marol',
    version='0.0.1',
    description='Run Python 3 code on AWS Lambda',
    long_description=readme,
    author='Rajiv Abraham',
    author_email='rajiv.abraham@gmail.com',
    url='https://github.com/scoremedia/marol',
    license=license,
    install_requires=['docker'],
    packages=find_packages(exclude=('tests', 'docs', 'venv')),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6'
    ]

)
