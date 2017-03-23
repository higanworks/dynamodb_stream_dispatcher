""" dynamodb_stream_dispatcher """
from setuptools import setup, find_packages


description = 'Dispatch dymamodb stream event to your functions.'
requires = open('requirements.txt').read().splitlines()

setup(
    name="dynamodb_stream_dispatcher",
    version='0.1.4',
    description=description,
    long_description=description,
    author="SAWANOBORI Yukihiko",
    author_email="sawanoboriyu@higanworks.com",
    url="https://github.com/higanworks/dynamodb_stream_dispatcher",
    license="MIT",
    packages=find_packages(),
    install_requires=requires
)
