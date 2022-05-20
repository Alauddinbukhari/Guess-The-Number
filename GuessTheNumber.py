from random import randint

logo ='''
   ___                       _____ _                __                 _               
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|   
                                                                                       
                                                                                                                                                                               
                                                                                       
'''

def solve(difficulty,choosen_number):
    attempt_Over=False
    attempts=difficulty
    while not attempt_Over:
        print(f'You have {attempts} attempts remaining to guess the number.') 
        guess_number=int(input('Make a guess:'))
        if guess_number==choosen_number:
            print(f'You got it! The answer was{choosen_number}')
            attempt_Over=True
        elif attempts==0:
            print('Your attempts are over')
            print('Game is over')
            print('You lose')
            attempt_Over=True

        
        
        
        elif guess_number<choosen_number:
            attempts-=1
            print('too low')
            print('Guess again')
        elif guess_number>choosen_number:
             attempts-=1
             print("You'r too high")
             print('Make a guess again')
       















print(logo)
print('Welcome to the Number Guessing Game')
print("I'm thinking of a number between 1 and 100")
choosen_number=randint(1,100)
print(choosen_number)
easy=5
hard=10
choosen_difficulty=input("Choose a difficulty.Type 'easy' or 'hard':").lower()

if choosen_difficulty=="easy":
    solve(easy,choosen_number=choosen_number)
elif choosen_difficulty=="hard":
    solve(hard,choosen_number=choosen_number)
