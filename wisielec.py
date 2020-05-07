import random

#stworzyc jeszcze funkcje ktora po trafieniu w litere, ktora wystepuje wiecej
# niz jeden raz, pokazywala wszystkie te litery od razu

list_of_word = ["mama", "tata", "cos tam", "haha", "lololol"]
rand_word = random.randint(0, len(list_of_word))
random_word_from_list = list_of_word[rand_word]

def hangman(word):
    wrong = 0
    stages = ["",
              "______         ",
              "|              ",
              "|      |       ",
              "|      0       ",
              "|     /|\      ",
              "|     / \      ",
              "|              "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Gra w wisielca")

    while wrong < len(stages):
        print("\n")
        char = input("odgadnij literę: ")
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n". join(stages[0: e]))
        if "_" not in board:
            print("wygrales!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print(f"Przegrales! miales odgadnax: {word}")


hangman(list_of_word[rand_word])






