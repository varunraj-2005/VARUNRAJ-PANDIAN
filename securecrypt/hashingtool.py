import hashlib

def hash_string(data, algo='sha256'):
    h = hashlib.new(algo)
    h.update(data.encode())
    return h.hexdigest()
