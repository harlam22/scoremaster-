from setuptools import setup, find_packages

setup(
    name='scormaster',
    version='0.1',
    description='A simple command-line task management application',
    author='harlam22',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'scormaster = scormaster.scormaster:main',
        ],
    },
    install_requires=[
        # List your dependencies here
    ],
)
