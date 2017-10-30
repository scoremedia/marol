# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='marol',
    version='0.0.4',
    description='Run Any Python 3 version on AWS Lambda',
    long_description=readme,
    python_requires='>=3.6',
    keywords='aws-lambda python3',
    author='Rajiv Abraham',
    author_email='rajiv.abraham@gmail.com',
    url='https://github.com/scoremedia/marol',
    license="Apache 2.0",
    install_requires=['docker'],
    packages=['marol'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6'
    ]

)
