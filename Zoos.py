s=input()
c=0
for i in s:
    if(i=="o"):
        break
    else:
        c+=1
d=len(s)-c
if(c*2==d):
    print("Yes")
else:
    print("No")