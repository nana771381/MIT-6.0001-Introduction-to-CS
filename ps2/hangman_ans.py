# Problem Set 2, hangman.py
# Name: Lo Yen Xuan
# Collaborators:
# Time spent: 4 hours

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    if letters_guessed[-1] in secret_word:
        return True
    else:
        return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    
   
    ans = ['_ '] * len(secret_word)
    
    for i in range(len(secret_word)):
        for letter in letters_guessed:
            if secret_word[i] == letter:
                ans[i] = letter
                
        
    return ' '.join(ans)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    alphabets = list(string.ascii_lowercase)
    
    for letters in letters_guessed:
        if letters in alphabets:
            alphabets.remove(letters)
    
    return ''.join(alphabets)

    
# additional helper function
def is_same (secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns a boolean value whether secret word is equal to secret word or not
    '''
    list(secret_word)
    
    for letter in secret_word:
        if not letter in letters_guessed:
            return False
        
    return True
    

# additional helper function
def unique_words (secret_word):
    '''
    secret_word: string, the word the user is guessing
    returns only the unique characters of secret words
    '''
    
    list(secret_word)
    unique = []
    
    for letter in secret_word:
        if letter not in unique:
            unique.append(letter)
    
    return ''.join(unique)

    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    num_guesses = 6
    
    # use secret_word instead
    s_word = secret_word
    
    warning = 3
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is" , len(s_word), "letters long.")
    
    print("You have" , warning, "warnings left.")
    print("-------------------------------")
    
    vowel = "aeiou"
    
    guess = []
    guessed_word_copy = ""
    
    
    
    while num_guesses > 0:
        
        print("You have", num_guesses, "guesses left.")
        print("Available letters:", get_available_letters(guess))
        
        attempt = input("Please guess a letter: ").lower()
        
        
        
        if not attempt in string.ascii_lowercase or attempt in guess:
            warning -= 1
            
            if warning < 0 :
                if attempt in string.ascii_uppercase:
                    print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", guessed_word_copy)
                
                else:
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", guessed_word_copy)
            
                num_guesses -= 1
            else:
                if not attempt in string.ascii_lowercase:
                    print("Oops! That is not a valid letter. You have", warning, "warnings left:", guessed_word_copy)
                    
                else:
                    print("Oops! You've already guessed that letter. You have", warning, "warnings left:", guessed_word_copy)
                
                
                
                
            print("----------------------")
            
            continue

        guess.append(attempt)
        guessed_word = get_guessed_word(s_word, guess)
        
                    
        if is_word_guessed(s_word, guess):
            num_guesses += 1
            print("Good guess:", guessed_word)
            
        else:
            if attempt in vowel:
                num_guesses -= 1
                
            print("Oops! That letter is not in my word:", guessed_word)
        
             
        guessed_word_copy = guessed_word
        
  
        print("----------------------")
        
        if is_same(s_word, guess):
            
            total_score = num_guesses + len(unique_words(s_word))
            
            print("Congratulations, you won!")
            print("Your total score for this game is:", total_score)
            
            break
        
        num_guesses -= 1
    
    if num_guesses <= 0:
        print("Sorry, you ran out of guesses. The word was", s_word, ".")
    
    




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

def remove(string): 
    return string.replace(" ", "") 

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
      
    my_word = remove(my_word)
    
    if len(my_word) != len(other_word):
        return False
    
    for i in range(len(other_word)):
        if my_word[i] == '_':
            continue
        
        if my_word[i] != other_word[i]:
            return False
    
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
  
    hints = []  
  
    for word in wordlist:
        if match_with_gaps(my_word, word):
            hints.append(word)
            print(word)
        
    if not hints:
        print("No matches found")
    
    



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    num_guesses = 6
    
    # use secret_word instead
    s_word = secret_word
    
    warning = 3
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is" , len(s_word), "letters long.")
    
    print("You have" , warning, "warnings left.")
    print("-------------------------------")
    
    vowel = "aeiou"
    
    guess = []
    guessed_word_copy = ""
    
    
    
    while num_guesses > 0:
        
        print("You have", num_guesses, "guesses left.")
        print("Available letters:", get_available_letters(guess))
        
        attempt = input("Please guess a letter: ").lower()
        
        if attempt == "*":
            show_possible_matches(guessed_word_copy)
            continue
        
        
        
        if not attempt in string.ascii_lowercase or attempt in guess:
            warning -= 1
            
            if warning < 0 :
                if attempt in string.ascii_uppercase:
                    print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", guessed_word_copy)
                
                else:
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", guessed_word_copy)
            
                num_guesses -= 1
            else:
                if not attempt in string.ascii_lowercase:
                    print("Oops! That is not a valid letter. You have", warning, "warnings left:", guessed_word_copy)
                    
                else:
                    print("Oops! You've already guessed that letter. You have", warning, "warnings left:", guessed_word_copy)
                
                
                
                
            print("----------------------")
            
            continue

        guess.append(attempt)
        guessed_word = get_guessed_word(s_word, guess)
        
                    
        if is_word_guessed(s_word, guess):
            num_guesses += 1
            print("Good guess:", guessed_word)
            
        else:
            if attempt in vowel:
                num_guesses -= 1
                
            print("Oops! That letter is not in my word:", guessed_word)
        
             
        guessed_word_copy = guessed_word
        
  
        print("----------------------")
        
        if is_same(s_word, guess):
            
            total_score = num_guesses + len(unique_words(s_word))
            
            print("Congratulations, you won!")
            print("Your total score for this game is:", total_score)
            
            break
        
        num_guesses -= 1
    
    if num_guesses <= 0:
        print("Sorry, you ran out of guesses. The word was", s_word, ".")
    
  



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
