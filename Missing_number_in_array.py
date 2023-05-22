for _ in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    l.sort()
    for i in range(a-1):
        if(l[i]!=(i+1)):
            print(i+1)
            break
    else:
        print(i+2)