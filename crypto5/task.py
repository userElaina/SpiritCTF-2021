# -*- coding: utf-8 -*-
# python 3.8.8

# Note: This program runs on the most powerful computer in the world.
#       The computer has over 2 ** 100 GB memory!

from secret import flag
from hashlib import md5
import random

huge_list = [i for i in range(2 ** 32)] #
choices = [random.choice(huge_list) for _ in range(1000)]

print(choices[:900])

assert flag.startswith("Spirit{") and flag.endswith('}')
assert flag[5:-1] == md5(str(sum(choices[900:])).encode()).hexdigest()