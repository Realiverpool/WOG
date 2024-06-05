import random
import app
from Scores.score import add_score


def generate_number(difficulty):
    return random.randrange(0, int(difficulty) + 1)


def get_guess_from_user(difficulty, snumber):
    user_guess = input(f'Enter a guess between 0 and {difficulty} \n'
                       'or type "*" to go back\n')
    if user_guess == '*':
        app.start_play()
        return user_guess, None
    else:
        return user_guess, compare_results(difficulty, snumber, user_guess)


def compare_results(difficulty, snumber, user_guess):
    if int(snumber) == int(user_guess):
        add_score(difficulty)
        print("Success")
        return True
    else:
        print("Incorrect")
        return False


def play(difficulty):
    snumber = generate_number(difficulty)
    user_guess, result = get_guess_from_user(difficulty, snumber)
    if result is not None:
        return result
