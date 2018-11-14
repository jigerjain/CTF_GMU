
Info func	[Check all the possible functions]
		[Any suspicious func? If yes keep the address handy]
Disass main	[Check where the buffer is been copied and which function is been used]
		[In this case, it is @0x0804887d]
Add breakpoint	[Insert it at location just before the call to strcpy]

Overflow the buffer
Info registers	[Check for ebp and esp addresses]
x/20xw $eax	[Check the buffer location on stack]
x/20xw $esp	[Check the stack pointer along with stack for any anomaly]
0x0804a438
0x080486e2


