import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

# Function to get the computer's choice
def computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Main function for the game
def main():
    user_score = 0
    computer_score = 0
    
    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions: Choose 'rock', 'paper', or 'scissors' for each round.")
    
    while True:
        # Get user input
        user_choice = input("\nEnter your choice (rock, paper, or scissors): ").lower()
        
        # Validate the user's input
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input! Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        # Generate computer's choice
        comp_choice = computer_choice()
        
        # Determine the winner
        result = determine_winner(user_choice, comp_choice)
        
        # Display choices and the result
        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {comp_choice}")
        print(result)
        
        # Update scores
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        # Display current scores
        print(f"\nCurrent Score: You - {user_score} | Computer - {computer_score}")
        
        # Ask if the user wants to play again
        play_again = input("\nDo you want to play another round? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Final Score:")
            print(f"You - {user_score} | Computer - {computer_score}")
            break

# Run the game
if __name__ == "__main__":
    main()
