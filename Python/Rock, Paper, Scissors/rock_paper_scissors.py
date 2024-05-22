import random

def main():
    while True: 
        # List of valid choices
        choices = ["rock", "paper", "scissors"]
        # Pick random choice as the choice of the computer
        computer = random.choice(choices)
        # Get users choice 
        user = None
        while user not in choices:
            user = input("Pick rock, paper, or scissors: ").lower()
        # Evaluate results or exit program
        check(computer, user)
        # Ask user if he/she wants to play again
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break
        else: 
            continue
    
    print("Thanks for playing!")


def check(computer, user):
    if user == computer:
        print(f"Computer picked: {computer}!")
        print("It's a tie!")
    elif user == "rock":
        if computer == "paper":
            print(f"Computer picked: {computer}!")
            print("You lost!")
        elif computer == "scissors":
            print(f"Computer picked: {computer}!")
            print("You won!")
    elif user == "paper":
        if computer == "scissors":
            print(f"Computer picked: {computer}!")
            print("You lost!")
        elif computer == "rock":
            print(f"Computer picked: {computer}!")
            print("You won!")
    elif user == "scissors":
        if computer == "rock":
            print(f"Computer picked: {computer}!")
            print("You lost!")
        elif computer == "paper":
            print(f"Computer picked: {computer}!")
            print("You won!")

main()