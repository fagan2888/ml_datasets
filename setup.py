from setuptools import setup, find_packages

setup(
    name = "ml_datasets",
    version = "0.0.1",
    author = "Zachary Chase Lipton",
    author_email = "zachary.chase@gmail.com",
    description = "A simple library for loading machine learning datasets",
    license = "MIT",
    keywords = "machine learning",
    install_requires = ['numpy'],
    packages=find_packages(
        '.'
    ),
    classifiers=[
    ],
)
