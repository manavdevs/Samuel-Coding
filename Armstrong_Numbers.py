n=int(input("enter a number"))
s=0
t=n
while t>0:
    d=t%10
    s+=d**3
    t//=10
if n==s:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

