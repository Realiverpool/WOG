def welcome():
    while True:
        username = input("Enter Username\n")
        if len(username) > 12 or len(username) < 4:
            print("Username must be between 4-12 characters")
        else:
            print(f"Hi {username} and welcome to the World Of Games: The Epic Journey")
            return username


def difficulty_menu():
    global difficulty
    difficulty = input("Please select difficulty level between 1-5\n"
                       "Type 'q' to go exit or '*' for game menu\n")
    while str(difficulty) != 'q' or str(difficulty) != '*':
        try:
            if str(difficulty) == 'q':
                print("Thank you for playing, Goodbye")
                return difficulty
            elif str(difficulty) == '*':
                start_play()
                return difficulty
            elif int(difficulty) > 5 or int(difficulty) == 0:
                print("Invalid number\n")
                difficulty_menu()
                return difficulty
            else:
                if int(game) == 1:
                    memory_game.play(difficulty)
                    if str(game) == 'q':
                        return game
                elif int(game) == 2:
                    guess_game.play(difficulty)
                    if str(game) == 'q':
                        return game
                elif int(game) == 3:
                    currency_roulette.play(difficulty)
                    if str(game) == 'q':
                        return game
        except ValueError:
            print("***ERROR***\n")
            difficulty_menu()
            return difficulty
# To check: The next 5 lines might be irrelevant
    if str(difficulty) == 'q':
        print("Thank you for playing, Goodbye")
    elif str(difficulty) == '*':
        start_play()
        return difficulty


def start_play():
    # To do: Add user score based on difficulty
    # global user_score
    global game
    # user_score = 0
    game = input("Please choose a game to play (1 = Memory Game, 2 = Guess Game, 3 = Currency Roulette):\n"
                 "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\n"
                 "2. Guess Game - guess a number and see if you chose like the computer.\n"
                 "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
                 "Type 'q' to exit or 'u' to change Username\n")
    while str(game) != 'q':
        try:
            if str(game) == 'q':
                return game
            elif str(game) == 'u':
                welcome()
                start_play()
                return game
            elif int(game) > 3 or int(game) == 0:
                print("Invalid number\n"
                      "Please choose a number between 1-3\n"
                      "Type 'q' to exit or 'u' to change Username\n")
                start_play()
                return game
            else:
                difficulty_menu()
                return game
        except ValueError:
            print("***ERROR***\n"
                  "Please choose a number between 1-3\n"
                  "Type 'q' to exit or '*' for game menu\n")
            start_play()
            return game
    print("Thank you for playing, Goodbye")



from Games import guess_game, currency_roulette, memory_game


def welcome():
    while True:
        username = input("Enter Username\n")
        if 4 <= len(username) <= 12:
            print(f"Hi {username} and welcome to the World Of Games: The Epic Journey")
            return username
        else:
            print("Username must be between 4-12 characters")


def difficulty_menu():
    global difficulty
    difficulty = input("Please select difficulty level between 1-5\n"
                       "Type 'q' to go exit or '*' for game menu\n")
    while str(difficulty) != 'q' or str(difficulty) != '*':
        if str(difficulty) == 'q':
            print("Thank you for playing, Goodbye")
            return difficulty
        elif str(difficulty) == '*':
            start_play()
            return difficulty
        elif int(difficulty) > 5 or int(difficulty) == 0:
            print("Invalid number\n")
            difficulty_menu()
            return difficulty
        elif int(difficulty) in [1, 2, 3, 4, 5]:
            if int(game) == 1:
                memory_game.play(difficulty)
                if str(game) == 'q':
                    return game
            elif int(game) == 2:
                guess_game.play(difficulty)
                if str(game) == 'q':
                    return game
            elif int(game) == 3:
                currency_roulette.play(difficulty)
                if str(game) == 'q':
                    return game
            else:
                print("***ERROR*** Invalid Option\n")
                difficulty_menu()
                return difficulty
        else:
            print("***ERROR*** Invalid Option\n")
            difficulty_menu()
            return difficulty
# To check: The next 5 lines might be irrelevant
#     if str(difficulty) == 'q':
#         print("Thank you for playing, Goodbye")
#     elif str(difficulty) == '*':
#         start_play()
#         return difficulty


def start_play():
    # To do: Add user score based on difficulty
    # global user_score
    global game
    # user_score = 0
    game = input("Please choose a game to play (1 = Memory Game, 2 = Guess Game, 3 = Currency Roulette):\n"
                 "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\n"
                 "2. Guess Game - guess a number and see if you chose like the computer.\n"
                 "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
                 "Type 'q' to exit or 'u' to change Username\n")
    while str(game) != 'q':
        if str(game) == 'q':
            return game
        elif str(game) == 'u':
            welcome()
            start_play()
            return game
        # elif int(game) > 3 or int(game) == 0:
        #     print("Invalid number\n"
        #           "Please choose a number between 1-3\n"
        #           "Type 'q' to exit or 'u' to change Username\n")
        #     start_play()
        #     return game
        elif int(game) in [1, 2, 3]:
            difficulty_menu()
            return game
        else:
            print("***ERROR*** Invalid Option\n"
                  "Please choose a number between 1-3\n"
                  "Type 'q' to exit or '*' for game menu\n")
            start_play()
            return game
    print("Thank you for playing, Goodbye")


from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello!'
if __name__ == '__main__':
    app.run(host='0.0.0.0')

from currency_converter import CurrencyConverter


def get_money_interval(difficulty):
    global rate, interval
    rate = CurrencyConverter().convert(1, 'USD', 'ILS')
    interval = 10 - int(difficulty)


def get_guess_from_user(difficulty):
    global number, guess
    number = random.randrange(1, 100)
    guess = input("Enter guess for the converted value of " + str(number) + "$ in ₪\n"
                                                                            "or type '*' to go back\n")
    if guess == '*':
        app.start_play()
        return guess
    else:
        compare_results(difficulty)
        if result is True:
            return True
        else:
            return False


def compare_results(difficulty):
    global result
    try:
        if int(guess) - int(interval) <= int(number) or int(number) <= int(guess) + int(interval):
            add_score(difficulty)
            print("success")
            result = True
        else:
            print("Incorrect")
            result = False
    except ValueError:
        print("Invalid guess, please enter numbers only\n")
        get_guess_from_user(difficulty)


def play(difficulty):
    get_money_interval(difficulty)
    get_guess_from_user(difficulty)


def generate_number(difficulty):
    global snumber
    snumber = random.randrange(0, int(difficulty))


def get_guess_from_user(difficulty):
    global user_guess
    user_guess = input(f'Enter a guess between 0 and {difficulty} \n'
                       'or type "*" to go back\n')
    if user_guess == '*':
        app.start_play()
        return user_guess
    else:
        compare_results(difficulty)
        if result is True:
            return True
        else:
            return False


def compare_results(difficulty):
    global result
    if int(snumber) == int(user_guess):
        add_score(difficulty)
        print("Success")
        result = True
    else:
        print("Incorrect")
        result = False


def play(difficulty):
    generate_number(difficulty)
    get_guess_from_user(difficulty)



import random
import time
from time import sleep
import app
from Scores.score import add_score
from Scores import utils


def generate_sequence(difficulty):
    global num_list
    num_list = random.sample(range(1, 100), int(difficulty))
    for i in range(len(num_list)):
        num_list[i] = str(num_list[i])


# def print_and_delete(list, duration):
#     print("Pay attention and try to remember the following number\\s")
#     sleep(0.7)
#     print(list, end='', flush=True)  # Print the message immediately without newline
#     time.sleep(duration)  # Wait for the specified duration
#     print('\r' + ' ' * len(list), end='', flush=True)  # Clear the output

def print_and_delete(list, duration):
    print("Pay attention and try to remember the following number\\s")
    sleep(0.7)
    print(list)
    time.sleep(duration)
    utils.screen_cleaner()


def get_list_from_user(difficulty):
    global user_list
    input_string = (input("Enter " + str(difficulty) + " number\\s between 1-100 separated by space\n"
                          "Press '*' to go back to game menu\n"))
    if str(input_string) == '*':
        app.start_play()
        return input_string
    else:
        user_list = input_string.split()
        is_list_equal(difficulty)
        if result is True:
            return True
        else:
            return False


def is_list_equal(difficulty):
    global result
    if str(num_list) == str(user_list):
        add_score(difficulty)
        print("Success")
        result = True
    else:
        print("Incorrect")
        result = False


def play(difficulty):
    generate_sequence(difficulty)
    print_and_delete(num_list, 0.7)
    get_list_from_user(difficulty)

