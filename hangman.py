name = input("Enter name:")
print("Welcome "+ name+ " time to play hangman!")

secret_word= "i am hacker"

guess_string = " "

lives =10

while lives > 0:

    character_left = 0

    for character in secret_word:
        if character in guess_string:
            print(character,end=" ")
        else:
            print("_",end=" ")
            character_left += 1


    print()

    if character_left ==0:
        print("You won!")
        break

    guess = input( "\nGuess a word:")
    if guess not in guess_string:
        guess_string += guess

    if guess not in secret_word:
        lives -=1
        print("Wrong guess!")
        print(f"You have {lives} left")

        if lives == 0 :
            print("You died!")
