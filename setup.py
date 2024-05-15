import setuptools

import os
current_dir = dir_setup = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir_setup, "groups", "version.py")) as f:
    exec(f.read())
del os

setuptools.setup(
    name = "groups",
    version = __version__,
    author = "Naman Taggar",
    description = "Study select groups in python",
    long_description = open("README.md").read(),
    long_description_content_type = "text/markdown",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = ">3.5"
)
