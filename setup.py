""" dynamodb_stream_dispatcher """
from setuptools import setup, find_packages

setup(
    name="dynamodb_stream_dispatcher",
    version='0.1.0',
    author="SAWANOBORI Yukihiko",
    author_email="sawanoboriyu@higanworks.com",
    url="https://github.com/higanworks/dynamodb_stream_dispatcher",
    license="MIT",
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines()
)
