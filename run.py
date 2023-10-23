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
if(first_choice == "yes"):
    print("Wise choice, this is not the place for you")
elif(first_choice == "no"):
    print("You decided to stay and you will be executed")
    print("GAME OVER")
else:
    print("Invalid choice, please enter yes or no")
    