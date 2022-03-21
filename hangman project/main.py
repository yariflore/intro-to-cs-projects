import re 
#regular expression library

#to create a comment on python command + 3
#get answer. 
# python doesnt need int or string to declare variable or SEMICOLON
answer_characters = "What's Up, Doc?" #7-3 changes, replaced array w a string
answer_characters = answer_characters.upper() 
# this will uppercase all letters so that we wont have to write all letters in uppercase


#TO KEEP TRACK WHAT LETTERS THE USER HAS MENTIONED
#answer guesses will store the boolean value of whether you have guessed it yet
#boolean value is true or false 
#at the moment all leters are false cause the user hasnt guessed true , 
#store known or unknown letters

answer_guesses = []

#for loop for answer_characters, commas apostrophes wil all be known already
# strick requirements: requires colon after declaration, and whatever you want under the for loop should be INDENTED

for current_answer_characters in answer_characters: 
  if re.search("^[A-Z]$", current_answer_characters) :
    answer_guesses.append(False)
  else:
    answer_guesses.append(True)

#logic of playing the game
    
guessed_letters = []
num_of_incorrect_guesses= 0

while num_of_incorrect_guesses < 5 and False in answer_guesses: 
  print ("---------------------------")
  print (" Guessed Letters:  ", end= "")

  
  for current_answer_characters in guessed_letters:
    print (f"{current_answer_characters} ", end = "")

  print()

  print (f"Number of Incorrect guesses remaining: { 5 - num_of_incorrect_guesses}")

  print()

  for answer_index in range(len(answer_characters)):
    if answer_guesses [answer_index]: 
      print (answer_characters[answer_index], end = "")
    else:
      print ("_", end= "")
      
  print ()
 
  letter = input ("enter a letter: ")
  
  letter = letter.upper()
  
  if letter not in guessed_letters and len(letter) == 1 and re.search("^[A-Z]$", letter):
    #make sure that the character you put in is an actual letter, now we need to see if the letter is in the puzzle
    guessed_letters_insert_index= 0

    for current_guessed_letter in guessed_letters:
      if letter > current_guessed_letter:
        break
        
      guessed_letters_insert_index +=1

    guessed_letters.insert(guessed_letters_insert_index, letter)
        
    if letter in answer_characters: 
      #letter is in the puzzle
      for current_answer_index in range(len(answer_characters)):
        #len returns the value in the array
        if letter == answer_characters[current_answer_index]:
          
          answer_guesses[current_answer_index] = True 
          #t in true has to be capitalized. this tells the programs at the current index,we have guessed the answer thus updating True
    else: 
      num_of_incorrect_guesses += 1 #python doesnt allow ++
         

#Game is over. Display whether user won or not
if num_of_incorrect_guesses < 5:
  print ("Congratulations, you solved the puzzle!")
else:
  print ("sorry, you ran out of guesses. ")

print (f"{answer_characters} is the answer to the puzzle") 