import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_score = 0
    computer_score = 0
    print(" Welcome to Rock-Paper-Scissors Game!")
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print(" Invalid choice. Please try again.")
            continue
        computer_choice = get_computer_choice()
        print(f"\n You chose: {user_choice}")
        print(f" Computer chose: {computer_choice}")
        result = get_winner(user_choice, computer_choice)
        print(" Result:", result)
        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1
        print(f"\nScore = You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("\n Thanks for playing! Final Score:")
            print(f" You: {user_score} | Computer: {computer_score}")
            break

main()
