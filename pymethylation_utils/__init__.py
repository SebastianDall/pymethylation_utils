__version__ = "v0.5.1"

import os
import platform
import urllib.request
import sys
import subprocess
import re

# Define the URL for the binary based on the platform
EPIMETHEUS_URL = {
    "Linux": "https://github.com/SebastianDall/epimetheus/releases/download/v0.5.0/epimetheus-linux",
    "Windows": "https://github.com/SebastianDall/epimetheus/releases/download/v0.5.0/epimetheus-windows.exe",
    "Darwin": "https://github.com/SebastianDall/epimetheus/releases/download/v0.5.0/epimetheus-macos",
}

def extract_version_from_url(url):
    match = re.search(r"v(\d+\.\d+\.\d+)", url)
    return match.group(1) if match else None

def check_installed_binary_version(path):
    try:
        result = subprocess.run(
            [path, "--version"], capture_output=True, text=True, check=True
        )
        version = result.stdout.strip()
        return version.split()[-1] if " " in version else None
    except Exception as e:
        print(f"failed to get version of epimetheus at {path}: {e}")
    
def download_epimetheus():
    """Download the binary from the provided URL to the destination path."""
    system = platform.system()
    binary_url = EPIMETHEUS_URL.get(system)
    if not binary_url:
        sys.exit(f"Unsupported platform: {system}")

    
    bin_dir = os.path.join(os.path.dirname(__file__), "bin")
    os.makedirs(bin_dir,exist_ok=True)
    
    dest_path = os.path.join(bin_dir, "epimetheus")
    if system == "Windows":
        dest_path += ".exe"

    installed_version = None
    if os.path.exists(dest_path):
        installed_version = check_installed_binary_version(dest_path)
        installed_version = installed_version

        expected_version = extract_version_from_url(binary_url)
        if installed_version != expected_version:
            print(f"Installed version ({installed_version}) does not match expected version ({expected_version})")
            print("Removing installed version")
            os.remove(dest_path)
        

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


download_epimetheus()
