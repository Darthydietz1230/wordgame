#Define the custom function "game_play"
def game_play():
    #open the text file 'all_words.txt' in read only mode and store the act of opening the file inside the variable 'valid_words'
    valid_words = open('all_words.txt', 'r')
    #read each line in the variable 'valid_words' and store that information inside the variable 'read'
    read = valid_words.readlines()
    #prompt the user for a guess and store that guess inside the variable 'guess'
    guess = input('Take a guess...')
    #open the variable 'guess' and change it so that the characters are all lower case and store that back inside the variable 'guess'
    guess = guess.lower()
    #create an empty list and call it by the name 'modified'
    modified = []
    #open the variable 'read' and interate through each 'line'
    for line in read:
        #append each 'line' to the list called 'modified' and strip all the white space from all sides of each 'line'
        modified.append(line.strip())
    #if the variable 'guess' exactly matches an element from the list called 'modified':
    if guess in modified:
        #print the variable 'guess'
        print(guess)
        #create a variable and name it 'valid' set it equal to True
        valid = True
        #create a variable and name it 'position' and set it equal to 0 - this will be a counter
        position = 0
        #create a variable called 'clue' and set it equal to an empty string
        clue = ""
        #recall the variable 'guess' and iterate through each 'letters'
        for letters in guess:
            #if the 'letters' are in the exact same position as the letters in 'secret-word'
            if letters == secret_word[position]:
                #add a '+' to the variable 'clue'
                clue += "+"
            #if 'letters' are in the variable 'secret_word' but not exactly in the correct position
            elif letters in secret_word:
                #add a '?' to the variable 'clue'
                clue += "?"
            #otherwise 
            else:
                #add a '-' to the variable 'clue'
                clue += "-"
            #add 1 to the variable 'position'
            position += 1
        #print the variable 'clue'
        print(clue)
        #while the variable 'clue' is exactly equal to '+++++'
        while clue == "+++++":
            #print 'You guessed the secret word! Great job!'
            print('You guessed the secret word! Great job!')
            #exit the script
            exit()
        #stop the iteration when the variable 'clue' exactly matches '+++++'
        return clue == "+++++"
    #otherwise
    else:
        #print 'Thats not a valid guess, try again!'
        print("That's not a valid guess, try again!")
        #the variable 'valid' is set to False
        valid = False
        #while the variable 'valid' is equal to False
        while valid == False:
            #recall the defined function 'game_play'
            game_play()
            #terminate the loop
            break

#print 'Welcome to the Word Guessing Game'
print('Welcome to the Word Guessing Game')
#print 'The rules are simple'
print('The rules are simple')
#print 'Guess the random 5-letter word within 6 attempts using the clues provided after each attempt'
print('Guess the random 5-letter word within 6 attempts using the clues provided after each attempt')

#load the 'random' Module
import random
#open the text file called 'target_words.txt' in read only mode and store it inside the variable called 'target_words'
target_words = open("target_words.txt", 'r')
#read each line in the variable called 'target_words' and store that information inside the variable called 'dictionary'
dictionary = target_words.readlines()
#open an empty list and call it 'mod_target'
mod_target = []
#for each 'word' in the variable 'dictionary'
for word in dictionary:
    #append that 'word' to the list called 'dictionary' and strip all the whitespace
    mod_target.append(word.strip())
#create a variable called 'secret_word' and choose a word at random from the list 'mod_target'
secret_word = random.choice(mod_target)
#open the variable 'secret_word' and change it so that the characters are all lower case and store that back inside the variable 'secret_word'
secret_word = secret_word.lower()
#print the variable 'secret_word'
#print(secret_word)

#create a variable and call it 'attempts' and set it to a value of 0 - this will be a counter
attempts = 0
#while the variable 'attempts' is less than 6
while attempts < 6 :
    #open the variable 'attempts' and add 1 to it
    attempts = attempts + 1
    #call the defined function 'game_play'
    game_play()

#print 'Sorry, you did not guess the secret word'
print('Sorry, you did not guess the secret word.')
#print'The secret word was, display the variable' secret_word''
print(f'The secret word was', secret_word)
