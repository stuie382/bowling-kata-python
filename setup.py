from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='bowling',
    version='0.1.0',
    description='Bowling Kata in Python',
    long_description=readme,
    url='https://github.com/stuie382/bowling-kata-python.git',
    packages=find_packages(exclude='tests')
)
