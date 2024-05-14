import random
import math
lower_range=int(input("Enter lower bound of the range: "))
upper_range=int(input("Enter upper bound of the range: "))
value=random.randint(lower_range,upper_range)
limit=math.log(upper_range-lower_range+1)
while(limit):
    guess=int(input("Enter your guess: "))
    if guess<value:
        print("Value guessed is too small")
        lower_range=guess
    elif guess>value:
        print("Value guessed is too large")
        upper_range=guess
    elif guess==value:
        print("Congratulations,You guessed it correct")
        break
    else:
        print("Better luck next time")
    
