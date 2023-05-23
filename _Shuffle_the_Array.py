n=int(input())
l=list(map(int,input().split()))
l1=l[0:(n//2)]
l2=l[(n//2)::]
for i in range(n//2):
    print(l1[i],l2[i],end=" ")