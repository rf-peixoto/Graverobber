from hashlib import sha256
import sys
try:
    node_id = str(sys.argv[1])
    node_sig = sys.argv[2]
    print(sha256(str(node_id + "some_secret_seed" + node_sig).encode()).hexdigest()[24:48][::-1])
except Exception as error:
    print("Usage:")
    print(sys.argv[0] + " node_id node_sig")
