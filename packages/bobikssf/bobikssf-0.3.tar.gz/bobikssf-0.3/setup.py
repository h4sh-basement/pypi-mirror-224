from setuptools import setup, find_packages

setup(
    name='bobikssf',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'requests',
        'Pillow'
    ],
)