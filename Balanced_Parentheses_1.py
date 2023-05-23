s=input()
a=[]
d={"(":")","{":"}","[":"]"}
for i in s:
    if(len(a)==0):
        a.append(i)
    elif(d[a[-1]]==i):
        a.pop()
    else:
        a.append(i)
if(len(a)==0):
    print(True)
else:
    print(False)