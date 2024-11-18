from setuptools import setup, find_packages

setup(
    name="cricinfo-stats",
    version="1.0.4",
    author="Ali Raza",
    author_email="aaraza1995@gmail.com",
    description="Python/Pandas Client for https://www.espncricinfo.com stats",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/aaraza/cricinfo",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Adjust as needed
    install_requires=[
        "pandas>=2.2.3",
        "requests>=2.32.3",
        "lxml>=5.3.0"
    ]
)