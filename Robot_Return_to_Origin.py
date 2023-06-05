a={'L':-1,'R':1,'D':2,'U':-2}
s=input()
su=0
for i in s:
    su+=a[i]
if(su==0):
    print(True)
else:
    print(False)