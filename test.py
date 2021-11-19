play = input("Would you like to play Hangman?(y/n): ")
wrong_input = 0
want_to_play = ["yes", "y", "no", "n"]
while play.lower() not in want_to_play:
  play = input("Sorry, that wasn't clear, please type either a y (for yes) or an n (for no): ")
  wrong_input += 1
  if wrong_input == 5:
    print("Sorry, I've already asked you 5 times! \nI still can't tell if you want to play or not, but I'm done trying!\nGoodbye!")
    break
if play.lower() == "y":
  print("Great! Lets get started!")
  import random
 # import time
 
  word_list = ["man", "fast", "apple", "family"]#need to add more words to list - POC for now 
  random_word = random.choice(word_list)
  random_word_plchldr = random_word

  blank_word = ""
  for i in range(len(random_word)):
    blank_word += ("_ ")
    #time.sleep(3)
  guessed_list = []
  total_guesses = 0
  empty_letter = "_"

  print(f"Looks like your SECRET WORD has {len(random_word)} letters in it. You have 15 guesses. Good luck!\n")
  while empty_letter in blank_word and total_guesses < 16:
    
    if len(guessed_list) == 0: #for first time entering a letter
      print("SECRET WORD: " + blank_word)
      guess = input("\nGuess a leter: ")
      total_guesses += 1
      guessed_list.append(guess)
    else:#for 2nd+ time entering a letter
      str_gussedlist = ', '.join(guessed_list)
      print("SECRET WORD: " + blank_word)
      guess = input(f"\nSo far you've guessed '{str_gussedlist}'. \nThat's {total_guesses} out of your 15 guesses, only {15 - total_guesses} left. \n\nGuess another leter: ")
      total_guesses += 1
      guessed_list.append(guess)
    
    if not guess.isalpha():
      print(f"You didn't enter a letter! That still cost you turn though! \nNow you've got {15 - total_guesses} left. Try again: ")    
    elif len(guess) > 1:
      print("You entered too many letters! \nOnly enter one letter at a time! \n(Sorry, but that still cost you a guess...)")
    elif guess in random_word:
      print("\n\nGood guess!")
      while guess in random_word_plchldr:  
        for i in random_word_plchldr:
                
          if guess is i:
             guessplcmnt = random_word_plchldr.find(guess) + 1
             blankindex = guessplcmnt*2-1
             #strings are immutable!!! can't use replace, you have to slice the strings and change it...
             blank_word = blank_word[:blankindex-1] + guess + blank_word[blankindex:]
             random_word_plchldr = random_word_plchldr[:guessplcmnt-1] + "9" + random_word_plchldr[guessplcmnt:]
    else:
      print("\nSorry, that letter isn't in the word!")
      print("Try again - ")
    
    if empty_letter not in blank_word:
      print("SECRET WORD :" + blank_word)
      print(f"Congratulations! you found the word! It was {random_word}.\nGAME OVER")
      break
    if total_guesses == 15:
      print(f"Sorry! that's all you're guesses!\n Your word was {random_word}.\nBetter luck next time. GAME OVER")
      break
    
if play.lower() == "n":
  print("OK, Goodbye, and have a great day!")

  #guesses_left = 15 - wrong_guesses
  #print("Wrong guesses = " + str(wrong_guesses) + ", you have " + str(guesses_left) + " left.")
  #print(blank_word)
#print(guess)
#print(random_word)



