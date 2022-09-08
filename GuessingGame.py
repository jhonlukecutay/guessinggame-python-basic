import random

#fruit list
fruitlist = ["watermelon", "lychee", "mango", "sineguelas", "grape", "apple", "banana", "citrus", "avocado", "durian"]

#random
ranFruit = random.choice(fruitlist)

#guess count and limit
guess_count = 0
guess_limit = 3

print("Guess what type of fruit is in 3 letters.")

while guess_count < guess_limit:
    print("")
    #last 3 letters.
    print("The fruit is " + str(ranFruit[-3:]) )
    print("")

    #user's answer
    print("Your answer is...")
    user_input = input()

    guess_count += 1
    
    if user_input == ranFruit:
        print("")
        print("Correct! The answer is " + ranFruit)
        #randomize.
        ranFruit = random.choice(fruitlist)
    else:
        print("")
        print("Wrong. The answer is " + ranFruit)
        #randomize.
        ranFruit = random.choice(fruitlist)

    if guess_count == guess_limit:
        print("You already tried 3 times. The program will end now.")




