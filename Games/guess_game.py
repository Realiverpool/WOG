import random
import app


def generate_number(difficulty):
    global snumber
    snumber = random.randrange(0, int(difficulty))


def get_guess_from_user(difficulty):
    global user_guess
    user_guess = input("Enter a guess between 0 and " + difficulty + "\n"
                       "or type '*' to go back\n")
    if user_guess == '*':
        app.start_play()
        return user_guess
    else:
        compare_results()
        if result is True:
            return True
        else:
            return False


def compare_results():
    global result
    if int(snumber) == int(user_guess):
        print("Success")
        result = True
    else:
        print("Incorrect")
        result = False


def play(difficulty):
    generate_number(difficulty)
    get_guess_from_user(difficulty)
