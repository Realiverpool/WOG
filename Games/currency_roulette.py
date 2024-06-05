from currency_converter import CurrencyConverter
import random
import app
from Scores.score import add_score


def get_money_interval(difficulty):
    rate = CurrencyConverter().convert(1, 'USD', 'ILS')
    interval = 10 - int(difficulty)
    return rate, interval


def get_guess_from_user(difficulty, rate, interval, number):
    guess = input(f"Enter guess for the converted value of {number}$ in ₪\n"
                  "or type '*' to go back\n")
    if guess == '*':
        app.start_play()
        return None, False
    elif guess.isdigit():
        return int(guess), compare_results(int(guess), number, rate, interval, difficulty)
    else:
        print("Invalid guess, please enter numbers only\n")


def compare_results(guess, number, rate, interval, difficulty):
    lower_bound = number * rate - interval
    upper_bound = number * rate + interval
    if lower_bound <= guess <= upper_bound:
        add_score(difficulty)
        return True
    else:
        return False


def play(difficulty):
    rate, interval = get_money_interval(difficulty)
    number = random.randrange(1,100)
    guess, result = get_guess_from_user(difficulty, rate, interval, number)
    if result:
        print(f"Your guess {guess} was correct!")
    else:
        print("Incorrect. Try again!")
