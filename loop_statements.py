for i in range(1,11):
    print(f"25*{i} = {25*i}")

print("----------------------------------")

n=int(input("Enter a number: "))
m= int(input("Enter a number: "))
for i in range (1,n+1):
    for j in range (1,m+1):
        print("*",end="")
    print()