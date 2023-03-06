import random
while True:

    user_choice = input("Choose rock (R), paper (P) or scissors (S): ")
    if user_choice == "R":
        print("you: rock")
    elif user_choice == "P":
        print("you: paper")
    elif user_choice == "S":
        print("you: scissors")

    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        print("computer: rock")
    elif computer_choice == 1:
        print("computer: paper")
    else:
        print("computer: scissors")

    if user_choice == "R" and computer_choice == 0:
        print("it's a draw!")
    elif user_choice == "R" and computer_choice == 1:
        print("computer won!")
    elif user_choice == "R" and computer_choice == 2:
        print("you won!")
    elif user_choice == "P" and computer_choice == 0:
        print("you won!")
    elif user_choice == "P" and computer_choice == 1:
        print("it's a draw!")
    elif user_choice == "P" and computer_choice == 2:
        print("computer won!")
    elif user_choice == "S" and computer_choice == 0:
        print("computer won!")
    elif user_choice == "S" and computer_choice == 1:
        print("you won!")
    elif user_choice == "S" and computer_choice == 2:
        print("it's a draw!")



    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
