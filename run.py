# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

print("Welcome to >>>Escape from prison<<< game")
print("---------------------------------------------")
print("2 months ago, you were framed for murder and in 3 days your execution is scheduled to take place in the merchant square.")
print("Only the two of us know perfectly well, that you are innocent and prison is no place for you.")
print("---------------------------------------------")
print("Will you be brave enough to escape from this terrible place? (yes/no)")

first_choice = input("> ")

if (first_choice == "yes"):
    print("Wise choice, this is not the place for you")
    print("Through a barred opening in the wall, you see rays of sunlight streaming into your cell. So it's almost noon.")
    print("Suddenly, from behind the metal door of your cell, you hear the sounds of guards leading another prisoner to the interrogation room.")
    print("As they pass by your cell, a fight begins between them.")
    print("As a result, one of the guards loses his keys.")
    print("---------------------------------------------")
    print("Are you brave enough to reach for it? (yes/no)")

    secend_choice = input("> ")

    if (secend_choice == "yes"):
        print("Well Done! You did it!")
        print("The prison corridor seems to be empty now.")
        print("---------------------------------------------")
        print("Do you want to use the keys and get out from your cell? (yes/no)")

        third_choice = input(">")

        if (third_choice == "yes"):
            print("It looks like your cell in the middle of a long, dark corridor.")
            print("The only way out is to go left or right.")
            print("---------------------------------------------")
            print("Where you want to go next? (left/right)")

            fourth_choice = input(">")

            if(fourth_choice == "left"):
                print("By taking the path leading left, you reaching the prison guard barracks.")
                print("You are immediately noticed by 4 opponents.")
                print("You are killed instantly.")
                print("GAME OVER")
            elif(fourth_choice == "right"):
                print("At the end of the right path, you see a guard sleeping in a chair.")
                print("Behind him, you see a door leading to the city streets.")
                print("To your freedom.")
                print("---------------------------------------------")
                print("Will you decide to sneak under the nose of a sleeping guard?")
                print("or do you want to turn back and try another escape route?")
                print("sneek/go back")
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
    