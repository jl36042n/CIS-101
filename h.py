import random
a = 30
b = int(input("How many people might show up?"))
c = random.randint(1,16)

food = ["Turkey","Apple Pie","Mashed Potatoes","Mac and Cheese"]
total = a+b+c
print("Welcome to my program for Thanksgiving")
answer = "n"
while answer !="y":
    for item in food:
        print("We need "+str(total)+" "+item)
    answer=input("Do you want to keep going? Type y to exit.")
