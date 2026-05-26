from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(
    name="ft_package",
    version="0.0.1",
    description="A sample test package",
    long_description=open('README.md').read(),
    author="Arno Baboomian",
    author_email="arbaboom@student.42yerevan.am",
    url="https://github.com/ababumyan/ft_package",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS independent",
    ],
    project_urls={
        "Bug Reports": "https://github.com/ababumyan/ft_package/issues",
        "Source": "https://github.com/ababumyan/ft_package",
    },
    python_requires=">=3.9, <4",
)
