import random
random_number=random.randint(1,100)

print("----------Welcome to the Number Guessing Game!----------")
print("                                                   ")
print("Try to guess the number I'm thinking of between 1 and 100.")

n=input("Enter your guess: ")

if int(n) == random_number:
    print("Congratulations! You've guessed the number correctly!")
    
else:
    print("Sorry, that's not correct. The number I was thinking of was:", random_number)

print("-----------------------------------------------------")

