n=input()
l=[]
c=0
for i in n:
    if(i.isdigit())and(i not in l):
        l.append(i)
        if(c==0):
            if(int(i)%2==0):
                c=1
if(c==0):
    print(-1)
else:
    a=''
    l.sort()
    if(int(l[0])%2==1):
        for j in range(1,len(l)):
            if(int(l[j])%2==0):
                l[j],l[0]=l[0],l[j]
                break
                
    for i in l[::-1]:
        print(i,end='')