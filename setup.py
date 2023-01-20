# -*- coding: utf-8 -*-

# Package and distribution management
# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='python boilerplate',
    version='0.1.0',
    description='Boilerplate template for Python',
    long_description=readme,
    author='Kiarash Soleimanzadeh',
    author_email='kiarash.s@hotmail.com',
    url='https://kiarashs.ir',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
