from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2","speech_recognition"]

setup(
    name="s2w",
    version="0.0.1",
    author="Eshan Agarwal",
    author_email="eshanagarwal12@gmail.com",
    description="A package that can convert a paragraph of spoken english to written english",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Eshan-Agarwal/Abbreviations-Conversion",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 2.7"
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3.0 (gpl-3.0)",
    ],
)