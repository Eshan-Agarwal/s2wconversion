from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2","SpeechRecognition>=3"]

setup(
    name="s2w",
    version="1.0.0",
    author="Eshan Agarwal",
    author_email="eshanagarwal12@gmail.com",
    description="A package that can convert a paragraph of spoken english to written english",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Eshan-Agarwal/Abbreviations-Conversion",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
       'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
       'Programming Language :: Python :: 3.4',
       'Programming Language :: Python :: 3.5',
       'Programming Language :: Python :: 3.6',
       "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    
)
