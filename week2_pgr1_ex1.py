import random       #import the module to simulate and randomize the computers choices
user_action = input("Enter a choice (rock, paper, scissors): ")
# here we are asking the user to input some action and save the input
# for later use
#You can use random.choice() to have the computer randomly select
# between the actions:
def main():
    count = 0
    while count < 3:
        count += 1
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    #This allows a random element to be selected from the list.
    # You can also print the choices that the user and the computer made:
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            
            print("Rock smashes scissors! You win!")
        else:
            
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            
            print("Paper covers rock! You win!")
        else:
            
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            
            print("Scissors cuts paper! You win!")
        else:
            
            print("Rock smashes scissors! You lose.")
            