'''
@author: badmonkey
@software: PyCharm
@file: badmonkey.py
@time: 2021/10/15 下午12:05
'''
import os
flag = os.getenv("FLAG")
flag = b"flag{dockerflag}" if not flag else flag.encode()

