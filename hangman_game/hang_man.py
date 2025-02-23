import random


def chose_word():
    words = ['python','java','kotlin','javascript']

    return random.choice(words).upper()


def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += ' _ '
    return display


def play():

    print('Welcome to Hangman Game!')
    word = chose_word()
    guessed_letters = set()
    attemptes = 6

    while attemptes > 0:

        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Attempts left: {attemptes}")

        guess = input('Input a letter:').upper()

        if guess in guessed_letters:
            print("You already Guessed this letter")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            attemptes -= 1
            print("That letter doesn't appear in the word")

        if all(letters in guessed_letters for letters in word):
            
            print(f"Congratulations! you guessed the word: {word}")
            break

    else:
        print("you Lost!!!")
        print("The Word was :",word)
if __name__ == "__main__":
    play()

    

