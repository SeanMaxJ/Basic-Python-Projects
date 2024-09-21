#Number Guessing Game
import random

x = random.randint(1,100)

def game() :
    guess = 0
    count = 0
    while guess != x :
        count += 1
        guess = int(input("\nEnter Your Guess ! (1 - 100) : "))
        if (guess > x) :
            print("Guess Lower !")
            
        elif (guess < x) :
            print("Guess Higher !")
            
        else :
            print("\nAffirmative, Good Job ;)\nAttempts : ", count)
            
print("\tSMJ's NUMBER GUESSING GAME !!!")
print("\t------------------------------")

while True : 
    game()
    print("\nThank You For Playing !")
    r = input(("\nWould You Like To Play Again ? (Yes/No) : "))
    if r.lower() == "no":
        print("\nSee You Again, Goodbye !!!\n")
        break
    elif r.lower() == "yes" :
        continue
    else : 
        print("\nError : Invalid Response !!!")        

    


