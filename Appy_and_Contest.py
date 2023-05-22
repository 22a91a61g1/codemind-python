t=int(input())
for _ in range(t):
    n,a,b,k=map(int,input().split())
    c=0
    for i in range(1,n+1):
        if(i%a==0 and i%b==0):
            continue
        elif(i%a==0):
            c+=1
        elif(i%b==0):
            c+=1
        if(c==k):
            print("Win")
            break
    else:
        print("Lose")