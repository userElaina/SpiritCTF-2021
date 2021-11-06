

from badmonkey import flag
from socketserver import BaseRequestHandler,ThreadingTCPServer
import random
import os
import string
from hashlib import sha256
import signal
from Crypto.Util.number import *

e = 65537
def rox(a,b,m):
    res=0
    ind=0
    while a or b:
        ar = a % m
        br = b % m
        a //= m
        b //= m
        res = res + ((ar - br) % m) * (m ** (ind))
        ind += 1
    return res


q=n//p

phi=(p-1)*(q-1)

d=inverse(e,phi)
_m=pow(c,d,n)

print(long_to_bytes(_m))