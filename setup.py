from setuptools import setup, find_packages

setup(
    name='log-analyzer',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'log_analyzer=log_analyzer.cli:main',
        ],
    },
)