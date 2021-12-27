from setuptools import setup
setup(
    name='halp',
    version='0.0.1',
    packages=['halp'],
    entry_points={
        'console_scripts': [
            'halp=halp.halp:main'
        ]
    }
)
