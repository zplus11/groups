import setuptools

setuptools.setup(
    name = "groups",
    version = "0.1.0",
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
    python_requires = ">3.5",
    py_modules = ["dihedral", "z", "u", "edp"]
)
