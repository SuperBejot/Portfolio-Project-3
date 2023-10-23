# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

print("Welcome to >>>Escape from prison<<< game")
name = input("Enter your name: ")
print("---------------------------------------------")
print("2 months ago, you", name, "were framed for murder and in 3 days your")
print("execution is scheduled to take place in the merchant square.")
print("Only the two of us know perfectly well, that you are innocent")
print("and prison is no place for you.")
print("---------------------------------------------")
print("Will you be brave enough to escape from this terrible place? (yes/no)")

first_choice = input("> ")

if (first_choice == "yes"):
    print("Wise choice, this is not the place for you")
    print("Through a barred opening in the wall, you see rays of sunlight")
    print("streaming into your cell. So it's almost noon.")
    print("Suddenly, from behind the metal door of your cell,")
    print("you hear the sounds of guards leading another prisoner")
    print("to the interrogation room.")
    print("As they pass by your cell, a fight begins between them.")
    print("As a result, one of the guards loses his keys.")
    print("---------------------------------------------")
    print("Are you brave enough to reach for it? (yes/no)")

    secend_choice = input("> ")

    if (secend_choice == "yes"):
        print("Well Done!", name, "You did it!")
        print("The prison corridor seems to be empty now.")
        print("---------------------------------------------")
        print("Do you want to use the keys to get out from the cell? (yes/no)")

        third_choice = input(">")

        if (third_choice == "yes"):
            print("It looks like your cell is in the middle")
            print("of a long, dark corridor.")
            print("The only way out is to go left or right.")
            print("---------------------------------------------")
            print("Where you want to go next", name, "? (left/right)")

            fourth_choice = input(">")

            if (fourth_choice == "left"):
                print("By taking the path leading left, you reaching")
                print("the prison guard barracks.")
                print("You are immediately noticed by 4 opponents.")
                print("You are killed instantly.")
                print("GAME OVER")
            elif (fourth_choice == "right"):
                print("At the end of the right path, you see")
                print("a guard sleeping in a chair.")
                print("Behind him, you see a exit door.")
                print("Maybe the door to your freedom.")
                print("---------------------------------------------")
                print("Will you sneak under the nose of a sleeping guard?")
                print("Or do you want to turn back")
                print("and try another escape route?")
                print("sneek/go back")

                fifth_choice = input("> ")

                if (fifth_choice == "sneek"):
                    print("The risk paid off!")
                    print("You escaped from prison!")
                    print("GAME OVER! Well Done!", name)
                elif (fifth_choice == "go back"):
                    print("You turn back")
                    print("but you end up straight in the hands of a guard")
                    print("who was checking around the prison.")
                    print("He put you back to your cell")
                    print("GAME OVER")
                else:
                    print("Invalid choice, please enter sneek or go back")
            else:
                print("Invalid choice, please enter left or right")

        elif (third_choice == "no"):
            print("What is wrong with you?")
            print("I was thinking you want to be free!")
            print("GAME OVER")
        else:
            print("Invalid choice, please enter yes or no")

    elif (secend_choice == "no"):
        print("I thought you wouldn't give up so easily.")
        print("GAME OVER")
    else:
        print("Invalid choice, please enter yes or no")

elif (first_choice == "no"):
    print("You decided to stay and you will be executed")
    print("GAME OVER")
else:
    print("Invalid choice, please enter yes or no")