def game():
    return 69

score = game()

with open(f"FILES/highscore.txt") as f:
    highscorestr = f.read()


if highscorestr=='':
    with open(f"FILES/highscore.txt",'w') as f:
        f.write(str(score))

elif int(highscorestr)<score:
    with open(f"FILES/highscore.txt",'w') as f:
        f.write(str(score))

