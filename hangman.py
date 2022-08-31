import random
from random import randint  # Do not delete this line


def displayIntro():
    into = open("hangman-ascii.txt", "r")
    for i in into.readlines()[0:23]:
        print(i.removesuffix('\n'))
    into.close()


def displayEnd(result):
    into = open("hangman-ascii.txt", "r")
    if result:
        for i in into.readlines()[190:203]:
            print(i.removesuffix('\n'))
    else:
        for i in into.readlines()[99:112]:
            print(i.removesuffix('\n'))
    into.close()


def displayHangman(state):
    into = open("hangman-ascii.txt", "r")
    if state == 5:
        for i in into.readlines()[23:33]:
            print(i.removesuffix('\n'))
    elif state == 4:
        for i in into.readlines()[36:46]:
            print(i.removesuffix('\n'))
    elif state == 3:
        for i in into.readlines()[49:59]:
            print(i.removesuffix('\n'))
    elif state == 2:
        for i in into.readlines()[62:72]:
            print(i.removesuffix('\n'))
    elif state == 1:
        for i in into.readlines()[75:85]:
            print(i.removesuffix('\n'))
    else:
        for i in into.readlines()[88:98]:
            print(i.removesuffix('\n'))


def getWord():
    file = open("hangman-words.txt", "r")
    words = file.readlines()
    return words[random.randint(0, len(words) + 1)]


def valid(c):
    return c.islower() and len(c) == 1


def play():
    lives = 5
    hiddenList = []
    word = getWord()
    displayHangman(lives)

    for i in range(0, len(word) - 1):
        hiddenList += '_'

    while lives > 0:

        if not hiddenList.__contains__("_"):
            return True

        print("Guess the word:  ", end='')
        for i in hiddenList:
            print(i, end='')
        print("\nEnter the letter:")

        c = input()
        while not valid(c):
            print("Invalid Input! Try Again!")
            c = input()
        if word.__contains__(c):
            for i in range(0, len(hiddenList)):
                if word[i] == c:
                    hiddenList[i] = c
        else:
            lives -= 1
        displayHangman(lives)

    displayHangman(0)
    print("Hidden word was:  " + word)
    return False


def hangman():
    while True:
        displayIntro()
        result = play()
        displayEnd(result)
        print("Do you want to play again? (yes/no)")
        answer = input()
        while answer != "yes" and answer != "no":
            answer = input()
        if answer == "no":
            break


if __name__ == "__main__":
    hangman()
