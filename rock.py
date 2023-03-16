import random

comp_wins = 0
player_wins = 0


def choose_option():
    user_choice = input("Choose Rock, Paper or Scissors: ")
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "s", "S"]:
        user_choice = "s"
    else:
        print("I don't understand, try again.")
        choose_option()
    return user_choice


def computer_option():
    comp_choice = random.randint(0,2)
    if comp_choice == 0:
        comp_choice = "r"
    elif comp_choice == 1:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice


while True:
    print("")

    user_choice = choose_option()
    comp_choice = computer_option()

    print("")

    if user_choice == "r":
        if comp_choice == "r":
            print(" You chose rock. Computer chose rock. It's a tie!")
        elif comp_choice == "p":
            print("You chose rock. Computer chose paper. Computer won!")
            comp_wins += 1
        elif comp_choice == "s":
            print("You chose rock. Computer chose scissors. You won!")
            player_wins += 1

    elif user_choice == "p":
        if comp_choice == "r":
            print("You chose paper. Computer chose rock. You won!")
            player_wins += 1
        elif comp_choice == "p":
            print("You chose paper. Computer chose paper. It's a tie!")
        elif comp_choice == "s":
            print("You chose paper. Computer chose scissors. Computer won!")
            comp_wins += 1

    elif user_choice == "s":
        if comp_choice == "r":
            print("You chose scissors. Computer chose rock. Computer won!")
            comp_wins += 1
        elif comp_choice == "p":
            print("You chose scissors. Computer chose paper. You won!")
            player_wins += 1
        elif comp_choice == "s":
            print("You chose scissors. Computer chose scissors. It's a tie!")


    print("")
    print("Player wins: " + str(player_wins))
    print("Computer wins: " + str(comp_wins))
    print("")


    user_choice = input("Do you want to play again? (y/n): ")
    if user_choice not in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        break
    else:
        break





