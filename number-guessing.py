import sys
import random
import time
from colorama import Fore, Style, init

arguments = sys.argv

def welcome():
    init()  # Initialize colorama
    print(Fore.CYAN + Style.BRIGHT + 
"""╔══════════════════════════════════════╗
║  Welcome to the Number Guessing Game!  ║
╚══════════════════════════════════════╝""" + Style.RESET_ALL)
    
    print(Fore.YELLOW + "\nI'm thinking of a number between 1 and 100.\n")
    print(Fore.GREEN + "Please select the difficulty level:\n")
    print(Fore.WHITE + "1. " + Fore.CYAN + "Easy   " + Fore.WHITE + "(10 chances)")
    print(Fore.WHITE + "2. " + Fore.YELLOW + "Medium " + Fore.WHITE + "(5 chances)")
    print(Fore.WHITE + "3. " + Fore.RED + "Hard   " + Fore.WHITE + "(3 chances)" + Style.RESET_ALL)

    game()

def get_difficulty_level():
    difficulty = input()
    valid = [1,2,3]

    if not difficulty.isdigit() or int(difficulty) not in valid:
        return Fore.RED + "Enter a valid difficulty, 1,2,3" + Style.RESET_ALL
    
    difficulty_num = int(difficulty)
   
    if difficulty_num == 1:
        return ["easy",10]
    
    if difficulty_num == 2:
        return ["medium",5]
    
    if difficulty_num == 3:
        return ["hard",3]
    
def generate_random():
    return random.randint(1, 100)

def game():
    try:
        difficulty = get_difficulty_level()
        if isinstance(difficulty, str):  # If error message
            print(difficulty)
            return game()
        
        random_number = generate_random()
        attempts = 0
        guessed = False

        for i in range(difficulty[1]):
            remaining = difficulty[1] - attempts
            print(Fore.CYAN + f"\nAttempts remaining: {remaining}" + Style.RESET_ALL)
            try:
                user_guess = int(input(Fore.YELLOW + "Enter your guess: " + Style.RESET_ALL))
            except ValueError:
                print(Fore.RED + "Please enter a valid number!" + Style.RESET_ALL)
                continue
            
            attempts += 1
            
            if user_guess == random_number:
                guessed = True
                print(Fore.GREEN + f"\n🎉 Congratulations! You guessed the correct number in {attempts} attempts! 🎉" + Style.RESET_ALL)
                break
            else:
                if user_guess > random_number:
                    print(Fore.RED + f"Incorrect! The number is less than {user_guess}." + Style.RESET_ALL)
                elif user_guess < random_number:
                    print(Fore.RED + f"Incorrect! The number is greater than {user_guess}." + Style.RESET_ALL)

        if not guessed:
            print(Fore.RED + "\n😔 Sorry, You ran out of chances!" + Style.RESET_ALL)
            print(Fore.YELLOW + f"The correct number was {random_number}" + Style.RESET_ALL)
        
        print(restart_game())
        
    except KeyboardInterrupt:
        print(Fore.CYAN + "\n\n👋 Thanks for playing! 👋" + Style.RESET_ALL)
        sys.exit(0)

def restart_game():
    try:
        restart_choice = input(Fore.CYAN + "\nDo you want to play again? (Y/N): " + Style.RESET_ALL)
        valid_restart = ["Y","N","y","n"]
        
        if restart_choice not in valid_restart:
            print(Fore.RED + "Please enter a valid choice" + Style.RESET_ALL)
            return restart_game()
        elif restart_choice.upper() == "Y":
            print(Fore.GREEN + "\nLet's play again!\n" + Style.RESET_ALL)
            print(Fore.YELLOW + "Enter the difficulty level: ")
            print(Fore.WHITE + "1. " + Fore.CYAN + "Easy   " + Fore.WHITE + "(10 chances)")
            print(Fore.WHITE + "2. " + Fore.YELLOW + "Medium " + Fore.WHITE + "(5 chances)")
            print(Fore.WHITE + "3. " + Fore.RED + "Hard   " + Fore.WHITE + "(3 chances)" + Style.RESET_ALL)
            game()
        else:
            return Fore.CYAN + "\n👋 Thanks for playing! 👋" + Style.RESET_ALL
        
    except KeyboardInterrupt:
        print(Fore.CYAN + "\n\n👋 Thanks for playing! 👋" + Style.RESET_ALL)
        sys.exit(0)

commands = {
    "start" : welcome
}

if len(arguments) == 2:
    commands[arguments[1]]()