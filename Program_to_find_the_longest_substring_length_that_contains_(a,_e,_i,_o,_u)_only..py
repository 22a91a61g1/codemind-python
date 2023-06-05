s=input()
ma=0
for i in range(len(s)):
    if(s[i] in "aeiou"):
        c=1
        for j in range(i+1,len(s)):
            if(s[j] in "aeiou"):
                c+=1
            else:
                break
        if(ma<c):
            ma=c
print(ma)