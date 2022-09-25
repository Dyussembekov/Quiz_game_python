secret_word = "Nurlan"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guess = False

while guess != secret_word and not(out_of_guess):  #if they havent guessed the secret word
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guess = True

        if out_of_guess:
            print("Out of guesses, u lose!")

print("U win!")