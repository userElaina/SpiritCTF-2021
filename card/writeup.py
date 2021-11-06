ans=0
for i in open('card.bin','rb').read():
    ans^=i
print(ans)