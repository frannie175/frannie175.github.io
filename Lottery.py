import random

print("*** Welcome to the £1m lottery ***")
print("The rules are simple:")
print("1. Pick seven numbers between 1 and 50")
print("2. Please enter your numbers one at a time, hit return after each number (no duplicates)")
print("3. The generator will show you the lottery numbers and let you know if you have won")


lottery_numbers = []
#we only want seven numbers
for i in range (0,7):
    number = random.randint(1,50)
    #make numbers unique now
    while number in lottery_numbers:
        number = random.randint(0,50)
    #now we make a list
    lottery_numbers.append(number)

#sort the numbers
lottery_numbers.sort()

user_numbers = []
#need to enter seven numbers
for i in range(0,7):
    number = int(input("What are your lottery numbers?"))
    #no duplicates
    while (number in user_numbers or number<0 and number>51):
        print("Invalid number, please enter number again")
        number = int(input("What are your lottery numbers?"))
    #add to list
    user_numbers.append(number)

#display list
print("Today's lottery numbers are {}".format(lottery_numbers))

print ("Your selection is {} ".format(user_numbers))

counter = 0
for number in user_numbers:
    if number in lottery_numbers:
        counter +=1

print ("you got {} matching numbers".format(counter))

if counter <= 2:
    print("You don't win anything this time")
elif counter == 3:
    print("You win £20")
elif counter == 4:
    print("You win £40")
elif counter == 5:
    print("You win £100")
elif counter == 6:
    print("You win £1000")
elif counter == 7:
    print("You win £1m")
