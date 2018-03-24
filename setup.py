from setuptools import setup, find_packages

setup(
    name='graphique',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A package to make plotly charts easier to use.',
    long_description=open('README.txt').read(),
    install_requires=['numpy', 'plotly', 'pandas'],
    url='https://github.com/mitchelllisle/graphique',
    author='Mitchell Lisle',
    author_email='lislemitchell at gmail'
)
