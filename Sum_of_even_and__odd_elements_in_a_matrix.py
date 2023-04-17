n,m=map(int,input().split())
mat=[]
s=0
s1=0
for i in range(n):
    lst=list(map(int,input().split()))
    mat.append(lst)
for i in range(n):
    for j in range(m):
        if mat[i][j]%2==0: s+=mat[i][j]
        else: s1+=mat[i][j]
print(s,s1)