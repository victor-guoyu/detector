from setuptools import setup

with open('test-requirements.txt') as f:
    tests_require = f.readlines()

setup(
    name='detector',
    version='1.0',
    description='A simple CLI tool that performs plagiarism detection using N-tuple comparison',
    author='Victor Guo',
    author_email='victor.guoyu@hotmail.com',
    packages=['detector'],
    tests_require=tests_require
)
