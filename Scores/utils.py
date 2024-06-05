import platform
import os

SCORES_FILE_NAME = "Scores/scores.txt"
BAD_RETURN_CODE = 414


def screen_cleaner():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
