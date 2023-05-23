s=input()
h=s[:2]
m=s[3:5]
f=s[-2]
t=""

if(f=="A"):
    if(int(h)==12):
        t+="00:"+m
    else:
        t+=h+":"+m
else:
    if(int(h)==12):
        t+="12:"+m
    else:
        h1=int(h)+12
        t+=str(h1)+":"+m
print(t)