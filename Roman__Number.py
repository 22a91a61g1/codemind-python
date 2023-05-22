num=int(input())
d = [(1,'I'),(4,'IV'),(5,'V'),(9,'IX'),
               (10,'X'),(40,'XL'),(50,'L'),(90,'XC'),
               (100, 'C'),(400,'CD'),(500, 'D'),(900, 'CM'),
               (1000, 'M')]
s=""  
l=len(d)-1
while(num):
    q=num//d[l][0]
    s+=d[l][1]*q
    num=num%d[l][0]
    l=l-1
print(s)