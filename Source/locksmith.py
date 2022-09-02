from hashlib import blake2s
import sys
try:
    node_id = str(sys.argv[1])
    node_sig = sys.argv[2]
    if int(node_id) % 2 == 0:
        print(blake2s(str(node_id + "some_secret_even_seed" + node_sig).encode()).hexdigest()[24:48][::-1])
    else:
        print(blake2s(str(node_id + "some_secret_odd_seed" + node_sig).encode()).hexdigest()[24:48][::-1])
except Exception as error:
    print("[*] Usage: " + sys.argv[0] + " [node_id] [node_sig]")
