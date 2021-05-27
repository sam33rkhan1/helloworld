#import random package
import random
#we define y as the number that has to be guessed
y = random.randint(1,101)
#we have to define x, but we will change this by user input
x = 0
#create the count variable
count = 0
#we create a loop and it will continue if the userinput is not 100
while x != y:
#we ask the user to input a number
        x = int(input("Try to guess the number: "))
#if the input is correct print this
        if x == y:
            count += 1 #when the answer is correct add 1 to count, because this is also a try
            print (x, "is perfect.", "You guessed it in", count, "times!") #when right, readout the amount of count and display it
#else if the input is lower print this
        if x < y:
            count += 1 #when the answer is to low add 1 to count
            print(x, "is to damn low!")
#else if the input is higher print this
        if x > y:
            count += 1 #when the answer is to high add 1 to count
            print(x, "is to damn high")