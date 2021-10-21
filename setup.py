from distutils.core import setup

setup(
    name='myapp',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'zzhack=scripts.cli:main'
        ]
    },
    packages=['scripts', 'scripts.functions']
)
