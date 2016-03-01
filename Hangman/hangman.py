#!/usr/bin/env python
import random
import webbrowser

#thing = 'a'
def convert_lower(thing):
    thing = thing.lower()
    return thing

def open_file():
    bool = "true"
    print "Welcome to hangman!!"
    while bool == "true":
        print "Enter easy, medium, or hard."
        choice = raw_input()
        choice = convert_lower(choice)
        if choice == "easy":
            hang = open("easy.txt")
            bool = "false"
        elif choice == "medium":
            hang = open("medium.txt")
            bool = "false"
        elif choice == "hard":
            hang = open("hard.txt")
            bool = "false"
        else:
            print "That wasn't an option. Try again."
            bool = "true"
    return hang
hang = open_file()
x = file.readlines(hang)

def get_random(x):
    rint = random.randint(0,len(x)-1)
    return rint

def random_word(x):
    rint = get_random(x)
    word = x[rint]
    return word
word = random_word(x)

def word_def(word):
    print "Would you like the definition of %s?, 'Y' or 'y' for yes, 'N' or 'n' for no" %word.strip()
    response = raw_input()
    response = convert_lower(response)
    if response == 'y':
        webbrowser.open('http://dictionary.reference.com/browse/%s?s=t' %word)

counter = [0]

def hang_the_man(counter, word):
    if counter[0] == 1:
        print "__________"
        print "|        |"
        print "|        O"
        print "|"
        print "|"
        print "__________"
    elif counter[0] == 2:
        print "__________"
        print "|        |"
        print "|        O"
        print "|        |"
        print "|"
        print "__________"
    elif counter[0] == 3:
        print "__________"
        print "|        |"
        print "|        O"
        print "|       -|"
        print "|"
        print "__________"
    elif counter[0] == 4:
        print "__________"
        print "|        |"
        print "|        O"
        print "|       -|-"
        print "|"
        print "__________"
    elif counter[0] == 5:
        print "__________"
        print "|        |"
        print "|        O"
        print "|       -|-"
        print "|       /"
        print "__________"
    elif counter[0] == 6:
        print "__________"
        print "|        |"
        print "|        O"
        print "|       -|-"
        print "|       / \\"
        print "__________"
        print ""
        print "You have died, too bad. The word was %s." %word.strip()
        word_def(word)

correct = []
def correct_letters(correct, word):
    for letter in (word.strip()):
        correct.append("_")
    return correct
correct = correct_letters(correct, word)

def check_guess(correct, word, counter):
    print correct
    print "Enter the letters you would like to guess one at a time."
    guess = raw_input()
    guess = convert_lower(guess)
    i = 0
    flag = False
    for letter in word:
        if guess == word[i]:
            correct[i] = guess
            flag = True
        i+=1
    if flag == False:
        counter[0]+=1

def win(corStr, word):
    if corStr == word.strip():
        print "Congratulations, you have saved the man!"
        word_def(word)
        return True
    else:
        return False


def check_loop(counter):
    while counter[0] != 6:
        corStr = "".join(correct)
        if win(corStr, word):
            break
        check_guess(correct, word, counter)
        c = (6 - counter[0])
        hang_the_man(counter, word)
        print "You have made %d incorrect guess(es), you have %s left." %(counter[0], c)

check_loop(counter)
