def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
a=int (input("Enter a number: "))
if a<0:
    print("Sorry factorials does not exist for a negative number ")
elif a==0:
    print ("Factorial of 0 is 1")
else:
    print("the factorial of ",a,"is ",factorial (a))