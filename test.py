n=input("Enter your input separated by spaces")
n=str(n)
l,s=[],[]
for d in n:
    l.append(int(d))
for i in range(0,4):
    x=[]
    for j in range(0,4):
        x.append(l.pop(0))
    s.append(x)
print(s[:])