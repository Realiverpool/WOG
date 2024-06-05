import os


def add_score(difficulty):
    points_won = int(difficulty) * 3 + 5
    current_points = 0

    if os.path.exists("Scores/Scores/scores.txt"):
        with open("Scores/Scores/scores.txt", "r") as file_read:
            content = file_read.read().strip()
            if content.isdigit():
                current_points = int(content)
    else:
        print("unable to find scores file")

    total_points = current_points + points_won

    with open("Scores/Scores/scores.txt", "w") as file_write:
        file_write.write(str(total_points))

    return difficulty
