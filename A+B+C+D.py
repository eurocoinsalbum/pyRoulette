import random
import time

money = []

for x in range(10):
    money.append(float(input("How much do you want to bet?\n")))

    user_choice = input('Do you choose 1-black or 2-red?\n')
    if (user_choice == 1):
        print("black")
        money -= []
    elif (user_choice == 2):
        print("red")
        money += []

    value = random.randint(1, 2)
    if (value == user_choice):
        money -= 100
    elif (value == 2):
        print("red")
        money += 100
   
    print("Amount: " + str(money))    
    time.sleep(1.)
