import random
attempt_list=[]
def show_score():
    if len(attempt_list) <= 0:
        print("There is currently no high score. It's yours for the taking!")
    else:
        print("Current high score is {} attempts".format(min(attempt_list)))

def start_game():
    random_number = int(random.randint(1,10))
    print("Hey there! Wlcome to the game of guesses!")
    player_name = input("Enter your name: ")
    wanna_play = input("{}, Do you wanna play the game? (Enter yes/no)".format(player_name))
    attempts = 0
    show_score()
    while wanna_play.lower()=="yes":
        try:
            guess = input("Pick a number between 1 and 10")
            if int(guess) <1 or int(guess)>10:
                raise ValueError("Please guess a number within given range")
            if int(guess)==random_number:
                print("Congrats! You guessed it right!")
                attempts+=1
                attempt_list.append(attempts)
                print("It took you {} attempts".format(attempts))
                play_again = input("Would you like to play agaim? (Enter yes/no)")
                attempts = 0
                random_number = int(random.randint(1,10))
                if play_again.lower()=="no":
                    print("That's cool, have a nice day!")
                    break

            elif int(guess) < random_number:
                print("It's lower")
                attempts+=1
            elif int(guess) > random_number:
                print("It's higher")
                attempts+=1

        except ValueError as err:
            print("Oh! That's not a valid Value. Try again")
            print("({})".format(err))
    else:
        print("That's cool, have a nice day!")

if __name__=='__main__':
    start_game()