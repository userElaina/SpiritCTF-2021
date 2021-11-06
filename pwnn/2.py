import re
from pwn import *

def solve(x:str)->bytes:
    
    s=x.decode('utf8').strip().split('.',1)[1][:-1].strip()
    print(s)
    if '(' in s:
        return b'0\n'
    else:
        return str(eval(s)).encode('utf8')+b'\n'

c = remote('202.198.27.90',20241)
for k in range(666):
    # c.recvuntil(b'Challenge!\n', drop=True)
    print(k,c.recvline())

    x=c.recvline()
    ans=solve(x)
    print(x,ans)
    c.send(ans)

print(k,c.recvline())
print(k,c.recvline())
print(k,c.recvline())
print(k,c.recvline())
