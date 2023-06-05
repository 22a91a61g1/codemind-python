s=input()
s=s[::-1]
c=""
b=0
d=""
for i in range(len(s)):
    if(s[i]!="#" and b==0):
        a=int(s[i])
        c+=chr(96+a)
    else:
        b+=1
        if(b>1):
            d+=s[i]
        if(b==3):
            a=int(d[::-1])
            c+=chr(96+a)
            b=0
            d=""
print(c[::-1])