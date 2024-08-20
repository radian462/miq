from setuptools import setup, find_packages

def requirements_from_file(file_name):
    return open(file_name).read().splitlines()

setup(
    name='miq',
    version='1.0.0',
    packages=find_packages(),
    install_requires=requirements_from_file('requirements.txt'),
    include_package_data=True,
)