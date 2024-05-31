from currency_converter import CurrencyConverter
import random
import app


def get_money_interval(difficulty):
    global rate, interval
    rate = CurrencyConverter().convert(1, 'USD', 'ILS')
    interval = 10 - int(difficulty)


def get_guess_from_user():
    global number, guess
    number = random.randrange(1,100)
    guess = input("Enter guess for the converted value of " + str(number) + "$ in ₪\n"
                  "or type '*' to go back\n")
    if guess == '*':
        app.start_play()
        return guess
    else:
        compare_results()
        if result is True:
            return True
        else:
            return False


def compare_results():
    global result
    try:
        if int(guess) - int(interval) <= int(number) or int(number) <= int(guess) + int(interval):
            print("success")
            result = True
        else:
            print("Incorrect")
            result = False
    except ValueError:
        print("Invalid guess, please enter numbers only\n")
        get_guess_from_user()


def play(difficulty):
    get_money_interval(difficulty)
    get_guess_from_user()
