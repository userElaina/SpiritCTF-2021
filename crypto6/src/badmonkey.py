import os
flag = os.getenv('FLAG')
flag = b"flag{dockerflag}" if not flag else flag.encode()
