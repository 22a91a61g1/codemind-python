s=list(input())
a=[]
for i in s:
    if(i.isalpha()):
        a.append(i)
a=a[::-1]
c=0
for j in range(len(s)):
    if(s[j].isalpha()):
        s[j]=a[c]
        c+=1
print(''.join(s))