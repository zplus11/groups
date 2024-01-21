import setuptools

setuptools.setup(
    name = "symmetries",
    version = "0.0.1",
    author = "Naman Taggar",
    description = "Study dihedral groups in python using permutations",
    long_description = open("README.md").read(),
    long_description_content_type = "text/markdown",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = ">3.5",
    py_modules = ["symmetries"]
)
