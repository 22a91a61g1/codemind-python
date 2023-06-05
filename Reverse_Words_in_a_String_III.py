s=input()
l=list(s.split(" "))
for i in range(len(l)):
    l[i]=l[i][::-1]
s=" ".join(l)
print(s)