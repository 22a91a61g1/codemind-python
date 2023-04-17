n,m=map(int,input().split())
mat=[]
s=0;s1=0
for i in range(n):
    lst=list(map(int,input().split()))
    mat.append(lst)
for i in range(n):
    if(i%2==0):
        for j in mat[i]:
            s+=j
    else:
        for j in mat[i]:
            s1+=j
print(s,s1)