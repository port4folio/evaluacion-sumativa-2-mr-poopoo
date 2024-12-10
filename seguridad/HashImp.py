# Hash Implementation V0.1

import hashlib

def HashEncode(msg):
    m = hashlib.sha256(bytes(msg,'utf-8')).hexdigest()
    #print('HashImp:')
    #print(str(m))
    return str(m)
