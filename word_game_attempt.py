#Wordle attempt 1
# figure out how to import a list of words.
# for now, will make a list and try to call a random word from it.


#import random
#dictionary = ['boots', 'happy', 'lager', 'monks', 'flops']

#print('Wordle: You have 6 attempts to guess a random 5 letter word')

#def cycle():
    #secret_word = random.choice(dictionary)
    #attempts = 6
    #while attempts > 0:
        #guess = input("Take a guess...")
        #guess = guess.lower()
        #if guess == secret_word:
            #print("You got the secret word!")
            #break

        #else:
            #attempts = attempts - 1
    #for letters in guess:
            #if letters in secret_word and letters in guess:
                #print(letters,'y')
            #elif letters in secret_word:
                #print(letters,'?')
            #else:
                #print(letters,'n')
    #if attempts == 0:
        #print("Sorry, you did not guess the secret word")
        #print("The secret word was:", secret_word)

def game_play():
    valid_words = open('all_words.txt', 'r')
    read = valid_words.readlines()
    guess = input('Take a guess...')
    guess = guess.lower()
    modified = []
    for line in read:
        modified.append(line.strip())
    if guess in modified:
        print(guess)
        valid = True
        position = 0
        clue = ""
        for letters in guess:
            if letters == secret_word[position]:
                clue += "+"
            elif letters in secret_word:
                clue += "?"
            else:
                clue += "-"
            position += 1
        print(clue)
        while clue == "+++++":
            print('You guessed the secret word! Great job!')
            exit()
        return clue == "+++++"
    else:
        print("That's not a valid guess, try again!")
        valid = False
        while valid == False:
            game_play()
            break


print('Welcome to the Word Guessing Game')
print('The rules are simple')
print('Guess the random 5-letter word within 6 attempts using the clues provided after each attempt')

import random
target_words = open("target_words.txt", 'r')
dictionary = target_words.readlines()
mod_target = []
for word in dictionary:
    mod_target.append(word.strip())
secret_word = random.choice(mod_target)
secret_word = secret_word.lower()
#print(secret_word)

attempts = 0
while attempts < 6 :
    attempts = attempts + 1
    game_play()

print('Sorry, you did not guess the secret word.')
print(f'The secret word was', secret_word)







