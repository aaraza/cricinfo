from setuptools import setup, find_packages

setup(
    name="cricinfo-stats",
    version="2.0.0",
    author="Ali Raza",
    author_email="aaraza1995@gmail.com",
    description="Python library for loading cricket statistics from ESPN Cricinfo into pandas DataFrames",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/aaraza/cricinfo",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
        "pandas>=2.2.3",
        "requests>=2.32.3",
        "lxml>=5.3.0",
        "html5lib>=1.1",
    ]
)