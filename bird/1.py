b=open('000.txt','rb').read()[83:-67]
print(b.hex())
print(int.from_bytes(b[-4:],'big'))
b=open('0.txt','rb').read()[83:-67]
print(b)
print(int.from_bytes(b[-4:],'little'))