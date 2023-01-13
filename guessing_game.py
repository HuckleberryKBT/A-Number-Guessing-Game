import random
from statistics import mean, median, mode

def print_greeting(greeting,attempts):
    print("-" * len(greeting) )
    print(greeting)
    #show best score if this is not the first attempt
    if len(attempts) > 0:
        print(f"The best score so far is:{min(attempts)}")
    print("-" * len(greeting))


def play_again():
    play_again = input("Would you like to play again? [Y/N] ")
    if play_again.upper() == "Y":
        return True
    else:
        print("Thank you for playing. Goodbye.")
        return False
       

def print_statistics(count, list):
    attempts_mean = mean(list)
    attempts_median = median(list)
    attempts_mode = mode(list)
    print(f"""
    Lets see how you did:
    Your score: {count}
    Mean: {attempts_mean}
    Median: {attempts_median}
    Mode: {attempts_mode}
    """)


def start_game():
  

    answer = random.randrange(1,100)
    attempts = []
    count = 0
    print_greeting("Welcome to the number guessing game.", attempts)
    while True:
        try:
            guess = int(input("Guess a number, you must: "))
            if guess < 1 or guess > 100:
                raise ValueError("Please guess a number between 1 and 100")
        except ValueError as err:
            print(f"Whoopsies, something went wrong. {err}. Please try again.")
        else:
            count += 1
            if guess > answer :
                print("It's lower")
            elif guess < answer:
                print("It's higher")
            elif guess == answer:
                print('*' * 40)
                print(f"You got it! It took you {count} attempts.")
                print('*' * 40)
                attempts.append(count)
                print_statistics(count, attempts)
                keep_playing = play_again()
                if keep_playing:
                    print_greeting("Going again? I like it!", attempts)
                    count = 0
                    answer = random.randrange(1,100)
                else:
                    break
        

start_game()