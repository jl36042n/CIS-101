import random
a=True
tries = 1
die1 = random.randint(1,6)
die2 = random.randint(1,6)
dice = die1 + die2
print("Welcome to the Rolling Dice Program!")
num = int(input("Enter a number 2 to 12: "))
print(num)
if(num < 2 or num > 12):
    a = False
    print("Not a real value for this game! Restart and try again!")
while a:
    dice = die1 + die2
    print("You input: " + str(num) + ", and the computer rolled " + str(dice))
    if (dice != num):
        die1 = random.randrange(6) + 1
        die2 = random.randrange(6) + 1
        tries = tries + 1
    else:
        print("Congrats, You Win After " + str(tries) + " Attempts!")
        a = False         
