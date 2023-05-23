n=int(input())
l=list(map(int,input().split()))
l=set(l)
l=sorted(l)[::-1]
if(len(l)>2):
    print(l[2])
else:
    print(l[0])