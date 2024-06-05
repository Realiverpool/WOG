import os
from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route('/')
def score_server():
    if os.path.exists("Scores/scores.txt"):
        with open("Scores/scores.txt", "r") as file_read:
            score = file_read.read().strip()
            if score.isdigit():
                return render_template('score_website.html',score=score)
            else:
                return render_template('score_website_error.html', error=utils.BAD_RETURN_CODE)
    else:
        return render_template('score_website_error.html', error=utils.BAD_RETURN_CODE)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
