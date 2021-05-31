"""
Heads Up

Our next goal is to learn how to read data from files. Loading data from a file can be useful for many final projects. Write a program that runs a console version of the phone game Heads Up!

How the game is played remotely:
When it is your turn, close your eyes. 

A word will be displayed in the HeadsUp program.

The rest of the section will try and describe it without saying the word.

You have to guess the word as quickly as possible.

Milestones:

Milestone #1: First, load all of the words from the file cswords.txt into a list.

Milestone #2: Then, show a randomly chosen word from the list

Milestone #3: Repeat: wait for the user to hit enter, then show another word.
"""

import random

# Name of the file to read in!
FILE_NAME = 'cswords.txt'

def get_words():
    list_of_words = []
    with open(FILE_NAME) as f:
        for line in f:
            list_of_words.append(line.strip())
    return list_of_words

def play_game(words):
    while True:
        input(random.choice(words))

def main():
    words = get_words()
    play_game(words)

if __name__ == '__main__':
    main()
