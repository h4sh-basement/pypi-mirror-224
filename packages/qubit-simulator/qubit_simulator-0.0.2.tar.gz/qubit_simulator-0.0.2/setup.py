from setuptools import setup, find_packages

setup(
    name="qubit_simulator",
    version="0.0.2",
    description="A simple qubit simulator",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Spencer Churchill",
    author_email="churchill@ionq.com",
    packages=find_packages(),
    install_requires=["numpy>=1.10.1"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
