import random

def play():
    choices = ["stone", "paper", "scissor"]
    user = input("Choose stone, paper or scissor: ").lower()
    
    if user not in choices:
        print("Invalid choice. Try again.")
        play()  # recursive call
        return

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (user == "stone" and computer == "scissor") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissor" and computer == "paper"):
        print("You win🥳✨!")
    else:
        print("You lose😖!")

    again = input("Do you want to play again? (y/n): ").lower()
    if again == "y":
        play()  # recursive call
    else:
        print("Thanks for playing!")

play()  # start the game
