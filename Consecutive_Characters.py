s=input()
ma=1
for i in range(len(s)-1):
    c=1
    for j in range(i+1,len(s)):
        if(s[i]==s[j]):
            c+=1
        else:
            break
    if(ma<c):
        ma=c
print(ma)