import random #importing random module

while True: #iterate loop
    user_action = input("enter choice(rock , paper ,scissors):") #take input
    possible_action = ["rock","paper","scissors"]
    #using random function
    computer_action = random.choice(possible_action)
    print(f"\nYou chose {user_action},computer chose {computer_action}.\n") #display both outputs what is selected by you and computer
    
#condtions to check who won the game
    if user_action == computer_action:
        print(f"Both players selected {user_action}.it's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win")
        else:
            print("paper covers rock! you lose")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win")
        else:
            print("Scissors cuts paper! You lose")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose")
#take input for playing again  
    play_again = input("PLay again? (y/n):")
    if play_again != "y":
        break