#!/usr/bin/env python3
from badmonkey import flag
from socketserver import BaseRequestHandler,ThreadingTCPServer
import random
import os
import string
from hashlib import sha256
import signal
from Crypto.Util.number import *


class Task(BaseRequestHandler):

    def send(self, msg,newline=True):
        try:
            if newline:
                msg += b'\n'
            self.request.sendall(msg)
        except:
            pass

    def _recv(self, sz):
        try:
            r = sz
            res = b""
            while r > 0:
                res += self.request.recv(r)
                if res.endswith(b"\n"):
                    r = 0
                else:
                    r = sz - len(res)
            res = res.strip()
        except:
            res = b""
        return res.strip(b"\n")

    def recv(self, sz,prompt=b"> "):
        self.send(prompt,newline=False)
        return self._recv(sz)

    def _recvall(self):
        BUFF_SIZE = 1024
        data = b''
        while True:
            _recv = self.request.recv(BUFF_SIZE)
            data += _recv
            if len(_recv) < BUFF_SIZE:
                break
        return data

    def recvall(self,prompt=b"> "):
        self.send(prompt,newline=False)
        return self._recvall()

    def close(self):
        self.send(b'see you next time~~')
        self.request.close()



    def proof_of_work(self):
        random.seed(os.urandom(8))
        proof = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(20)])
        _hexdigest = sha256(proof.encode()).hexdigest()
        self.send(f"sha256(XXXX+{proof[4:]}) == {_hexdigest}".encode())
        x = self.recvall(prompt=b'Give me XXXX: ')
        if len(x) != 4 or sha256(x + proof[4:].encode()).hexdigest() != _hexdigest:
            return False
        return True



    def handle(self):
        signal.alarm(120)
        if not self.proof_of_work():
            return
        p = getPrime(1024)
        q = getPrime(1024)
        n = p * q
        e = 0x10001
        h1 = p>>724
        h2 = q%(2**300)
        m = bytes_to_long(flag)
        c = pow(m, e, n)
        self.send(b"welcome to  crypto challenge 6.")
        self.send(b"can you get flag from me?")
        self.send(b"c = " + str(c).encode())
        self.send(b"e = " + str(e).encode())
        self.send(b"n = " + str(n).encode())
        self.send(b"h1 = " + str(h1).encode())
        self.send(b"h2 = " + str(h2).encode())
        self.close()

if __name__ == '__main__':
    HOST, PORT = "0.0.0.0", 10000
    server = ThreadingTCPServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()



