from setuptools import setup, find_packages
from setuptools.command.install import install
import os
import platform
import urllib.request
import sys

# Define the URL for the binary based on the platform
METHYLATION_UTILS_URL = {
    "Linux": "https://github.com/SebastianDall/methylation_utils/releases/download/v0.2.3/methylation_utils",
    "Windows": "https://github.com/SebastianDall/methylation_utils/releases/download/v0.2.3/methylation_utils.exe",
    "Darwin": "https://github.com/SebastianDall/methylation_utils/releases/download/v0.2.3/methylation_utils",
}

def download_methylation_utils(url, dest_path):
    """Download the binary from the provided URL to the destination path."""
    try:
        print(f"Attempting to download binary from {url}...")
        urllib.request.urlretrieve(url, dest_path)
        print("Download completed successfully.")
        # Make the file executable for Unix-like systems
        if platform.system() != "Windows":
            os.chmod(dest_path, 0o755)
    except urllib.error.URLError as e:
        print(f"Failed to download binary from {url}. URL Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while downloading binary: {e}")
        sys.exit(1)

class InstallCommand(install):
    """Custom installation command to download the methylation_utils binary."""
    def run(self):
        # Determine the binary URL based on the platform
        system = platform.system()
        binary_url = METHYLATION_UTILS_URL.get(system)
        if not binary_url:
            sys.exit(f"Unsupported platform: {system}")

        # Define the destination path for the binary
        bin_dir = os.path.join(self.install_lib, "methylation_utils_wrapper", "bin")
        os.makedirs(bin_dir, exist_ok=True)
        dest_path = os.path.join(bin_dir, "methylation_utils")
        if system == "Windows":
            dest_path += ".exe"

        # Download the binary
        download_methylation_utils(binary_url, dest_path)

        # Continue with the standard installation
        super().run()

setup(
    name="pymethylation_utils",
    version="v0.1.0",
    description="Python wrapper for the methylation_utils Rust binary",
    author="Sebastian Dall",
    author_email="semoda@bio.aau.dk",
    packages=find_packages(),
    include_package_data=True,
    cmdclass={
        'install': InstallCommand,
    },
    install_requires=[],
)

