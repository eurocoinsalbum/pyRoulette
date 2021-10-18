import random
import time

money = []

for x in range(10):
    money.append(float(input("How much do you want to bet?\n")))
    user_choice = input('Do you choose 1-black or 2-red?\n')

    random.choice = random.randint(1, 2)
    if (choice == 1):
        print("black")
        money -= []
    elif (choice == 2):
        print("red")
        money += [6]

    print("Amount: " + str(money))    
    time.sleep(1.)
