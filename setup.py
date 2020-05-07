import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="py-shiprocket",
    version="0.1.1",
    description="The unofficial shiprocket api python wrapper",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/DefCon-007/py-shiprocket",
    author="Ayush Goyal",
    author_email="ayushgoyal.iitkgp@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["shiprocket"],
    include_package_data=True,
    install_requires=["requests"],
)