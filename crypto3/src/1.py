import re
from pwn import *
from hashlib import sha256

from Crypto.Util.number import *
c = remote('202.198.27.90',20145)
# nc 202.198.27.90 20145
s=''
while not s.startswith('sha256'):
    s=c.recvline().decode('utf8')

l=re.findall('\+[a-zA-Z0-9]+\)',s)[0][1:-1]
r=s.strip().split(' == ')[1].strip()

strings=string.ascii_letters + string.digits
def f():
    for i0 in strings:
        for i1 in strings:
            for i2 in strings:
                for i3 in strings:
                    _s=(i0+i1+i2+i3+l).encode('utf8')
                    if sha256(_s).hexdigest()==r:
                        c.sendline(_s)
                        return 

f()


s=''
while not s.startswith('c'):
    s=c.recvline().decode('utf8')

_c=int(s.strip().split(' = ')[1].strip())


s=''
while not s.startswith('n'):
    s=c.recvline().decode('utf8')

n=int(s.strip().split(' = ')[1].strip())


s=''
while not s.startswith('leak'):
    s=c.recvline().decode('utf8')

leak=int(s.strip().split(' = ')[1].strip())
r = int.from_bytes(b"spirit_2021_crypto_challenge_233333", byteorder="big")


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

p=rox(leak,r,7)
q=n//p

phi=(p-1)*(q-1)

d=inverse(e,_phi)
_m=pow(_c,d,n)

print(long_to_bytes(_m))