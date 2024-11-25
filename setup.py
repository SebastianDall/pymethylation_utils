from setuptools import setup, find_packages

setup(
    name="pymethylation_utils",
    version="v0.2.4",
    description="Python wrapper for the methylation_utils Rust binary",
    author="Sebastian Dall",
    author_email="semoda@bio.aau.dk",
    packages=find_packages(),
    include_package_data=True,
    package_data={'pymethylation_utils': [
        "bin/*"
    ]},
    install_requires=[],
)

