#!/usr/bin/python3
from random import choice
from time import sleep
from os import name, system
from english_words import english_words_lower_alpha_set

def print_screen(man, word, letters_chosen, words_chosen):
  print_letters_chosen = ""
  print_words_chosen = ""
  for i in range(len(words_chosen)):
    for j in range(len(words_chosen[i])):
      print_words_chosen += words_chosen[i][j]
    print_words_chosen += " "
  for i in range(len(letters_chosen)):
    print_letters_chosen += f"{letters_chosen[i]} "
  system(clear)
  print(man)
  whole_word = "\n"
  for i in range(len(word)):
    whole_word = whole_word + word[i] + " "
  print(whole_word)
  if len(print_letters_chosen) == 0:
    print(print_words_chosen)
  else:
    print(print_letters_chosen + print_words_chosen)

def guess(man, print_word, word, letters_chosen, words_chosen):
  while True:
    print_screen(man, print_word, letters_chosen, words_chosen)
    guess_word = input().lower()
    if len(guess_word) == len(word) and guess_word not in words_chosen:
      break
    elif len(guess_word) != 1:
      print("Try a word that's the same length as this one")
      sleep(2)
      continue
    elif not guess_word.isalpha():
      print("That is not a letter in the alphabet!")
      sleep(2)
      continue
    elif guess_word in letters_chosen or guess_word in print_word:
      print("You've tried that letter before!")
      sleep(2)
      continue
    elif guess_word in words_chosen:
      print("You've tried that word before!")
      sleep(2)
      continue
    else:
      break
  return guess_word

def check_guess(guess_word, word, print_word, wrong, letters_chosen, words_chosen):
  if len(guess_word) == 1:
    if word.__contains__(guess_word):
      for i in range(len(word)):
        if word[i] == guess_word:
          print_word[i] = guess_word
    else:
      wrong += 1
      letters_chosen.append(guess_word)
  else:
    if guess_word == word:
      for i in range(len(guess_word)):
        print_word[i] = guess_word[i]
    else:
      words_chosen.append(guess_word)
      wrong += 1
  return print_word, wrong, letters_chosen, words_chosen

def main():
  word = "1"
  while not word.isalpha():
    word = choice(list(english_words_lower_alpha_set))
  letters_chosen = []
  print_word = []
  words_chosen = []
  for i in range(len(word)):
    print_word.append("_")

  man = ["______\n\n\n\n\n", "______\n  | \|\n\n\n\n", "______\n  | \|\n     |\n\n\n", "______\n  | \|\n     |\n     |\n\n", "______\n  | \|\n     |\n     |\n     |\n", "______\n  | \|\n     |\n     |\n     |\n======", "______\n  | \|\n  O  |\n     |\n     |\n======", "______\n  | \|\n  O  |\n  |  |\n     |\n======", "______\n  | \|\n  O  |\n /|  |\n     |\n======", "______\n  | \|\n  O  |\n /|\ |\n     |\n======", "______\n  | \|\n  O  |\n /|\ |\n /   |\n======", "______\n  | \|\n  O  |\n /|\ |\n / \ |\n======"]

  wrong = 0
  tries = 1
  
  guess_word = guess(man[wrong], print_word, word, letters_chosen, words_chosen)
  print_word, wrong, letters_chosen, words_chosen = check_guess(guess_word, word, print_word, wrong, letters_chosen, words_chosen)
  
  while guess_word != word and print_word.__contains__("_"):
    if wrong+1 == len(man):
      break
    guess_word = guess(man[wrong], print_word, word, letters_chosen, words_chosen)
    tries += 1
    print_word, wrong, letters_chosen, words_chosen = check_guess(guess_word, word, print_word, wrong, letters_chosen, words_chosen)
  print_screen(man[wrong], word, letters_chosen, words_chosen)
  if wrong+1 == len(man):
    print(f"Wrong! The word was {word}")
  else:
    if tries == 1:
      try_word = "try"
    else:
      try_word = "tries"
    print(f"Correct! It took you {tries} {try_word}")

if __name__ == "__main__":
    if name == "posix":
        clear = "clear"
    else:
        clear = "cls"
    main()
