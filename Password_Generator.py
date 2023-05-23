l=list(input().split(","))
p=""
for i in l:
    s=''
    for j in range(len(i)):
        if(i[j]==":"):
            break
        else:
            s+=i[j]
    n=i[j+1:]
    n=sorted(n)[::-1]
    a=len(s)
    for k in n:
        if(int(k)<=a):
            p+=s[int(k)-1]
            break
    else:
        p+="X"
print(p)