s="3a2c3a35152538272c2d213e332e3c25383030373a15"
c=[0x6a,0x6f,0x6e,0x73,0x6e,0x6f,0x77,0x69,0x73,0x64,0x72,0x61,0x67,0x6f,0x6e,0x62,0x79,0x62,0x69,0x72,0x74,0x68]

flag=[]
for i in range(0,len(s),2):
    flag.append(int("0x"+s[i:i+2],16))
    

newflag=""
for i in range(len(c)):
    temp=c[i]^flag[i]
    newflag+=chr(temp)
print(newflag)