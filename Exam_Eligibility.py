print ("--------------------Questions #1-4---------------------")

a=int(input("enter your age - "))

b=int(input("enter your average mark score - "))

c=str(input("Do you have a degree or diploma from a Designated Learning Institution (DLI)? - "))

d=str(input("Do you have a valid government-issued photo ID? - "))

print ("--------------------Eligibility Result---------------------")

if a>=18 and b>69 and c=="yes" and d=="yes":
    print ("You are eligible for an exam")
else:
    print ("You are not eligible for an exam")