def fact(f):
    su=0
    for i in range(1,int(f**(0.5))+1):
        if(f%i==0):
            su+=i
            if(i!=(f//i)):
                su+=f//i
    return(su)
a=[]
l=list(map(int,input().split(",")))
for i in l:
    s=fact(i)
    if(s in l):
        a.append(i)
a=sorted(a)
if(len(a)==0):
    print(-1)
else:
    print(*a)