for _ in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    for i in range(a):
        if(i==0):
            sl=0
            sr=sum(l[i+1::])
            if(sl==sr):
                print("YES")
                break
        elif(i==a-1):
            sr=0
            sl=sum(l[0:a-1])
            if(sl==sr):
                print("YES")
                break
        else:
            sl=sum(l[0:i])
            sr=sum(l[i+1:])
            if(sl==sr):
                print("YES")
                break
    else:
        print("NO")