from setuptools import setup, find_packages
from setuptools.command.build_py import build_py
import os
import platform
import urllib.request
import sys

# Define the URL for the binary based on the platform
METHYLATION_UTILS_URL = {
    "Linux": "https://github.com/SebastianDall/methylation_utils/releases/download/v0.2.4/methylation_utils-linux",
    "Windows": "https://github.com/SebastianDall/methylation_utils/releases/download/v0.2.4/methylation_utils-windows.exe",
    "Darwin": "https://github.com/SebastianDall/methylation_utils/releases/download/v0.2.4/methylation_utils-macos",
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

class BuildCommand(build_py):
    """Custom build command to download the binary during the build process."""
    def run(self):
        # Determine the binary URL based on the platform
        system = platform.system()
        binary_url = METHYLATION_UTILS_URL.get(system)
        if not binary_url:
            sys.exit(f"Unsupported platform: {system}")

        # Define the destination path for the binary
        bin_dir = os.path.join("methylation_utils_wrapper", "bin")
        dest_path = os.path.join(bin_dir, "methylation_utils")
        if system == "Windows":
            dest_path += ".exe"

        # Download the binary
        download_methylation_utils(binary_url, dest_path)

        # Continue with the standard build
        super().run()

setup(
    name="pymethylation_utils",
    version="v0.1.4",
    description="Python wrapper for the methylation_utils Rust binary",
    author="Sebastian Dall",
    author_email="semoda@bio.aau.dk",
    packages=find_packages(),
    include_package_data=True,
    package_data={'methylation_utils_wrapper': [
        "bin/*"
    ]},
    cmdclass={
        'build_py': BuildCommand,
    },
    install_requires=[],
)

