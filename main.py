import random
import time

for x in range(10):
    value = random.randint(1, 2)
    if (value == 1):
        print("black")
    elif (value == 2):
        print("red")
    
    time.sleep(1.)
