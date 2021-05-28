"""The python wrapper for Salla API package setup."""
from setuptools import (setup, find_packages)

setup(
    name="salla_api",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["requests", "requests_cache", "rich", "pydantic"],
    include_package_data=True,
    description="Salla.sa API for Python",
    long_description="Salla.sa API for Python",
    url="https://github.com/mdn522/salla_api",
    author="Abdullah Mallik",
    author_email="mdn522@gmail.com",
    zip_safe=False
)
