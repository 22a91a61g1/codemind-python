s=input()
h=s[:2]
m=s[3:5]
t=""

if(h=="00"):
    t+="12:"+m+" AM"
elif(h=="12"):
    t+="12:"+m+" PM"
elif(int(h)<12):
    t+=h+":"+m+" AM"
elif(int(h)>12):
    h1=int(h)-12
    if(h1==12):
        t+="12:"+m+" PM"
    elif(h1<10):
        t+="0"+str(h1)+":"+m+" PM"
    else:
        t+=str(h1)+":"+m+" PM"
print(t)