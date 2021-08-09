# Stack Zero Writeup

[Run binary 

Opening in Ghidra, we look at the functions list and look at "main"

[Insert picture of ghidra results]

Looking at the decompiled C code, we can see that we want to overwrite [insert var name] from the value zero, to anything else.

We can see that the stack representation of the variables show that [insert variable name] (our input string buffer) is 0x40 or 64 bytes away from the [insert overwrite variable name].

### python -c "print('A'*0x40 + '\xad\xde\xef\xbe')" | ./stackzero.c.o 
