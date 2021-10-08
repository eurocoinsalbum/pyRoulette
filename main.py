import random
import time

money = 100

for x in range(10):
    value = random.randint(1, 2)
    if (value == 1):
        print("black")
        money -= 100
    elif (value == 2):
        print("red")
        money += 100

    print("Amount: " + str(money))    
    time.sleep(1.)
