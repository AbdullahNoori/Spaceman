import random

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    is_guessed = True

    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return is_guessed

def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += "_"
    return guessed_word

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet


def is_guess_in_word(guess, secret_word):
    if guess in secret_word:
        return True
    else:
        return False


def get_input_letter():
    while True:
        letter = input("Enter a letter : ")
        letter = letter.lower()
        if len(letter) == 1 and letter.isalpha():
            return letter
        else:
            print("You entered invalid letter, try again! ")





def spaceman(secret_word):
    guess = 7
    is_the_word_guessed = False
    input_letters = []
    input_letters_as_a_string = ""


    print("Welcome to Spaceman!")
    wordlength = len(secret_word)

    print(secret_word)
    print("the secret word contains: " + str(wordlength) + " letters")
    print("---------------------------------------------------------------------")

    while guess > 0 and is_the_word_guessed == False:
        print("You have " + str(guess) +  " strikes left, choose wisely.")

        input_letter = get_input_letter()
        input_letters.append(input_letter)
        input_letters_as_a_string += input_letter

        if is_guess_in_word(input_letter, secret_word_in_chars):
            print("Congrats! You chose the right letter")

            if is_word_guessed(secret_word_in_chars, input_letters):
                is_the_word_guessed = True
        else:
            guess = guess - 1
            print("Incorrect guess")



    if is_the_word_guessed == False:
        print("Sorry, game is over. You lose. The word was: " + secret_word)

    else:
        print("Congrats! You win! ")

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost





#These function calls that will start the game
# secret_word = load_word()
# secret_word_in_chars = list(secret_word)
# spaceman(secret_word)
# print("would you like to play again?")
# answer =  input("Enter Yes/No:")
# while answer == "Yes" or answer == "No":
#     secret_word = load_word()
#     spaceman(secret_word)
#     answer = input("Enter Yes/No: ")
