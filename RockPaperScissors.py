import random

def main():
    count = 0
    while count < 5:
        count += 1    # count = count + 1
            
        user = input("Enter 'rock', 'paper', or 'scissor': ")

        while user != "rock" and user != "paper" and user != "scissor":
            user = input("Please Enter 'rock', 'paper', or 'scissor': ")

        comp_choice = random.randint(1,3)

        cc_converted = convert(comp_choice)
        print(cc_converted, 'is what the computer chose.')

        comparator(user, cc_converted)

def convert(value):
    if value == 1:
        return "rock"
    elif value == 2:
        return "paper"
    else:
        return "scissor"

def comparator(user, computer):
    if user == "rock" and computer == "scissor":
        print('You win! Rock beats scissors.')
    elif user == "scissor" and computer == "paper":
        print('You win! Scissors beats paper.')
    elif user == "paper" and computer == "rock":
        print('You win! Paper beats rock')
    elif user == "scissor" and computer == "rock":
        print('You lose! Rock beats scissors.')
    elif user == "paper" and computer == "scissor":
        print('You lose! Scissors beats paper.')
    elif user == "rock" and computer == "paper":
        print('You lose! Paper beats rock.')
    else:   
        print('Tie game.')




main()

