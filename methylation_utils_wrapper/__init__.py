__version__ = "v0.2.1"

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

def download_methylation_utils():
    """Download the binary from the provided URL to the destination path."""
    system = platform.system()
    binary_url = METHYLATION_UTILS_URL.get(system)
    if not binary_url:
        sys.exit(f"Unsupported platform: {system}")

    
    bin_dir = os.path.join(os.path.dirname(__file__), "bin")

    if not os.path.exists(bin_dir, exist_ok=True):
        os.makedirs(bin_dir)
    
    dest_path = os.path.join(bin_dir, "methylation_utils")
    if system == "Windows":
        dest_path += ".exe"


    if not os.path.exists(dest_path):
        try:
            print(f"Attempting to download binary from {binary_url}...")
            urllib.request.urlretrieve(binary_url, dest_path)
            print("Download completed successfully.")
            # Make the file executable for Unix-like systems
            if platform.system() != "Windows":
                os.chmod(dest_path, 0o755)
        except urllib.error.URLError as e:
            print(f"Failed to download binary from {binary_url}. URL Error: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred while downloading binary: {e}")
            sys.exit(1)


download_methylation_utils()
