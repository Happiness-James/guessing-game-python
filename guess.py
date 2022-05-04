
from email.mime import nonmultipart
from operator import truediv
import random

while True:
    flag = True
    while flag:
        num  = input('Type a number from an upper bound: ')

        if num.isdigit():
            print("let's play!")
            num = int(num)
            flag = False
        else:
            print("invalid input try again!") 

    secret = random.randint(1,num)

    guess = None
    count = 1

    while guess != secret:
        guess = input('please type a number between 1 and ' + str(num) + ": ") 

        if guess.isdigit():
         guess = int(guess)

        if guess == secret:
         print("yaaay! you've got it!")
        else:
         print("Ooops!try again!")
        count +=1
    print("it took you", count, "guesses!")            
