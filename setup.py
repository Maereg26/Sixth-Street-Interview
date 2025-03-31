from setuptools import setup, find_packages

setup(
    name = "Stock_fetcher_library",
    version = "0.1"
    packages = find_packages(),
    description = "Python library to fetch stock quotes.",
    install_requires = ["requests"],
    author = "Maereg Habtezgi",
    author_contact = "maeregh19@gmail.com",
)
