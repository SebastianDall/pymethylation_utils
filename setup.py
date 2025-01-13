from setuptools import setup, find_packages

setup(
    name="pymethylation_utils",
    version="v0.5.0",
    description="Python wrapper for the epimetheus Rust binary",
    author="Sebastian Dall",
    author_email="semoda@bio.aau.dk",
    packages=find_packages(),
    include_package_data=True,
    package_data={'pymethylation_utils': [
        "bin/*"
    ]},
    install_requires=[],
)

