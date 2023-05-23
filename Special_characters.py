s=input()
c=0
e=""
o=""
for i in s:
    if(i.isdigit()):
        if(int(i)%2==0):
            e+=i
        else:
            o+=i
    elif(i.isalnum()==False):
        c+=1
if(c%2==0):
    if(len(e)>len(o)):
        for j in range(len(o)):
            print(e[j],end="")
            print(o[j],end="")
        print(e[j+1:])
    else:
        for j in range(len(e)):
            print(e[j],end="")
            print(o[j],end="")
        print(o[j+1:])
else:
    if(len(e)>len(o)):
        for j in range(len(o)):
            print(o[j],end="")
            print(e[j],end="")
        print(e[j+1:])
    else:
        for j in range(len(e)):
            print(o[j],end="")
            print(e[j],end="")
        print(o[j+1:])