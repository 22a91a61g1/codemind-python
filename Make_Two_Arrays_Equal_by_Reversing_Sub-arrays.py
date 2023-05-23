n1=int(input())
l1=list(map(int,input().split()))
n2=int(input())
l2=list(map(int,input().split()))
if(n1!=n2):
    print(False)
else:
    for i in l1:
        if(i not in l2)or(l2.count(i)!=l1.count(i)):
            print(False)
            break
    else:
        print(True)