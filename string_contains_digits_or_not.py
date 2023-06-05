for _ in range(int(input())):
    a=input()
    for i in a:
        if(i.isdigit()):
            print("Yes")
            break
    else:
        print("No")