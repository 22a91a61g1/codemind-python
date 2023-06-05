s=input()
d={'b':0,'a':0,'l':0,'o':0,'n':0}
for i in s:
    if(i in d):
        d[i]+=1
d['l']=d['l']//2
d['o']=d['o']//2
print(min(d.values()))