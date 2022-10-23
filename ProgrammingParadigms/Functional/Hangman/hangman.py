import os
# clear console
cls = lambda: os.system('cls' if os.name=='nt' else 'clear')
# game structure
createGame = lambda word, progress, guessedLetters, mistakes: (word, progress, guessedLetters, mistakes)
# check if the letter is in the list of guessed letters
alreadyGuessed = lambda game, char: char in game[2]
# creates the initial string of unknown letters
progressString = lambda word: "+" * len(word)
# if a word (could be a guess, or the completed progress word) is equal to the original word
gameWinCheck = lambda game, word: game[0] == word
# if 7 mistakes are made, lose
gameLostCheck = lambda game: game[3] == 7
# if a character in the progress string isnt a +, it means it already got guessed, so keep it
# then, if the character guessed is equal to the character in the word, add it
# if none of the previous things, then it isnt a correct guess for the character, put a +
individualProgressChar = lambda wordChar, progressChar, char: progressChar if progressChar != "+" else char if char == wordChar else "+"
# create a list of letters for the new progress word, then join them together to make the new progress word
generateProgress = lambda word, progress, char: "".join([individualProgressChar(word[x], progress[x], char) for x in range(len(word))])
# forward the game on a correct guess, creates new progress word and adds the char to the guessed chars list
updateGame = lambda game, char: (game[0], generateProgress(game[0], game[1], char), game[2] + [char], game[3])
# forward the game on a mistake, if its a word, no new characters are added
addMistake = lambda game, char: (game[0], game[1], game[2] + [char], game[3] + 1) if len(char) == 1 else (game[0], game[1], game[2], game[3] + 1)
# if the guess is in the word, update progress, if it isnt, add a mistake
guess = lambda game, char: updateGame(game, char) if char in game[0] else addMistake(game, char)

programRunning = True

while programRunning:
    print("Hangman")
    print("Press Enter to start new game")
    input("")
    word = input("Type a word: ")
    newGame = createGame(word.lower(), progressString(word), [], 0)
    gameRunning = True
    while gameRunning:
        cls()
        print("Word: " + newGame[1])
        print("Mistakes: " + str(newGame[3]))
        print("Type the option you want to do")
        print("1. Guess a letter")
        print("2. Guess the word")
        option = input()
        if option == "1":
            char = input("Type a letter: ")
            if alreadyGuessed(newGame, char):
                print("You already tried this letter")
            else:
                newGame = guess(newGame, char)
            if gameWinCheck(newGame, newGame[1]):
                print("You won! The word was " + newGame[0])
                gameRunning = False
            elif gameLostCheck(newGame):
                print("You lost The word was " + newGame[0])
                gameRunning = False
        elif option == "2":
            word = input("Type a word: ")
            if gameWinCheck(newGame, word):
                print("You won! The word was " + newGame[0])
                gameRunning = False
            else:
                newGame = addMistake(newGame, word)
            if gameLostCheck(newGame):
                print("You lost! The word was " + newGame[0])
                gameRunning = False
    continueGame = input("Type 1 to play again, anything else to quit: ")
    if continueGame != "1":
        programRunning = False
