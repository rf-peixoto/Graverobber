from hashlib import sha256
import sys

node_id = str(sys.argv[1])
node_sig = sys.argv[2]

if not node_id:
    print(sys.argv[0] + " node_id + node_sig")
else:
    print(sha256(str(node_id + "some_secret_seed" + node_sig).encode()).hexdigest()[24:48][::-1])
