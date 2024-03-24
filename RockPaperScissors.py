#Create a Rock, Paper, Scissors game in Python using random, time and os modules.
import random
import time
import os
total_choices=["rock","paper","scissors"]
tot_rounds=14
round=1
user_score=0
computer_score=0
while round<=tot_rounds+1:
    computer_choice=random.choice(total_choices)
    if round==tot_rounds+1:
        if user_score>computer_score:
            print("Congrats! You Won the Game")
        elif user_score<computer_score:
            print("Sorry! Computer Wins")
        else:
            print("It's a tie")
        print("Game Over")
        break
    else:
        if user_score==7 or computer_score==7:
            if user_score>computer_score:
                print("Congrats! You Won the Game")
            elif user_score<computer_score:
                print("Sorry! Computer Wins")
            else:
                print("It's a tie")
            print("Game Over")
            break
        else:
            print("Round",round)
            print("User Score: ",user_score)
            print("Computer Score: ",computer_score)
            user_choice=input("Please enter your choice(Rock, Paper, Scissors): ").lower()
            if user_choice==computer_choice:
                print("It's a tie!")
                print("Computer's choice: ",computer_choice)
                print("Your choice: ",user_choice   )
                time.sleep(2)
                os.system("cls")
            elif user_choice=="rock" and computer_choice=="scissors":
                print("Rock beats Scissors! You win!")
                print("Computer's choice: ",computer_choice)
                print("Your choice: ",user_choice   )
                user_score+=1
                time.sleep(2)
                os.system("cls")
            elif user_choice=="paper" and computer_choice=="rock":
                print("Paper beats Rock! You win!")
                print("Computer's choice: ",computer_choice)
                print("Your choice: ",user_choice   )
                user_score+=1
                time.sleep(2)
                os.system("cls")
            elif user_choice=="scissors" and computer_choice=="paper":
                print("Scissors beats Paper! You win!")
                print("Computer's choice: ",computer_choice)
                print("Your choice: ",user_choice   )
                user_score+=1
                time.sleep(2)
                os.system("cls")
            else:
                if computer_choice=="rock" and user_choice=="scissors":
                    print("Rock beats Scissors! Computer wins!")
                    print("Computer's choice: ",computer_choice)
                    print("Your choice: ",user_choice   )
                    computer_score+=1
                    time.sleep(2)
                    os.system("cls")
                elif computer_choice=="paper" and user_choice=="rock":
                    print("Paper beats Rock! Computer wins!")
                    print("Computer's choice: ",computer_choice)
                    print("Your choice: ",user_choice   )
                    computer_score+=1
                    time.sleep(2)
                    os.system("cls")
                elif computer_choice=="scissors" and user_choice=="paper":
                    print("Scissors beats Paper! Computer wins!")
                    print("Computer's choice: ",computer_choice)
                    print("Your choice: ",user_choice   )
                    computer_score+=1
                    time.sleep(2)
                    os.system("cls")
            round+=1