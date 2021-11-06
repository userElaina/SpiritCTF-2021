M=7
ans=list()
for i in range(M):
    for j in range(i,M):
        print(i,j,i*j%M,(i+j)%M)
        ans.append((i*j%M,(i+j)%M))


print(len(ans),len(set(ans)))