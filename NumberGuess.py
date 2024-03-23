#importing of random module
import random
print("Welcome to Number Guessing Game")
print("May I know your name? before we start the game")
#input function is used to take user's name as input
name = input()
print("Hello",name)
#Rules of the game
print("In this game there are 10 rounds and with every round the difficulty level increases, with every correct guess of the number you gain 10 points and you will have 10 chances to guess the number in each round. If you guess the number in 1st attempt you will get 10 points, if you guess the number in 2nd attempt you will get 9 points and so on. If you are unable to guess the number in 10 attempts you will get 0 points.")
#Initialization of score
score = 0
#Initialization of rounds
rounds = 10
#variable to increment the range of random number after every round
n = 10  
print("Let's start the game")
for i in range(1,rounds+1):
    #generating random number
    generated_number = random.randint(1,n)
    print("Round",i)
    print("Guess the number between 1 and",n)
    for j in range(1,11):
        if 1<=j<=9:
            #taking user's guess as input
            guess = int(input())
            if guess == generated_number:
                print("Congratulations! You have guessed the number in",j,"attempts")
                score+=10-j
                break
            elif guess < generated_number:
                if generated_number - guess <= 5:
                    print("The number is very close to",guess)
                else:
                    print("The number is greater than",guess)
            else:
                if guess - generated_number <= 5:
                    print("The number is very close to",guess)
                else:
                    print("The number is smaller than",guess)
        #if it is the last attempt
        elif j == 10:
            guess = int(input())
            #if the user guesses the number correctly in the last attempt
            if guess == generated_number:
                print("Congratulations! You have guessed the number in",j,"attempts")
                score+=10-j
            else:
                print("You have exhausted all your attempts. The number was",generated_number)
                print("Let's move to the next round")
    #After every round the range of random number is incremented by 10
    n+=10
#Displaying the final score of the user
print("Your final score is",score)
#If the user's score is greater than or equal to 80 then he/she wins the game
if score >= 80:
    print("Congratulations! You have won the game")
print("Game Over")