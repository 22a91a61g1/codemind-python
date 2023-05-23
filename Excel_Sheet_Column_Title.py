n=int(input())
s=""
a=64
while(n!=0):
    s+=chr((n%26)+a)
    n=n//26
print(s[::-1])