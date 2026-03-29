x=int(input("enter your number"))
print ("this is the number",x)

if x% 2==0:
    print ("the number is even")
else:
    print ("the number is odd")

print ("-------------------------")
a=float (input ("enter your height"))
b=float (input ("enter your weight"))
c= b/(a/100)**2
if c<=18.4:
    print ("You are underweight")
elif c<=24.9:
    print ("You are healthy!")
elif c<=39.9:
    print ("You are obese")
else:
    print ("You are severely obese")

print ("---------------------------")
a=int(input("enter you number"))
if a>50:
    if a%2==0:
        print ("the number is even")
    else:
        print ("the number is odd")
else: print ("please enter a number greater than 50")