a=[]
for _ in range(int(input())):
    s=input()
    for i in range(len(s)):
        if(s[i]==""):
            break
    l=s[0:i]
    d=s[i::]
    l=l.replace(".","")
    for j in range(len(l)):
        if(l[j]=="+"):
            l=l[0:j]
            break
    g=l+d
    a.append(g)
print(len(set(a)))