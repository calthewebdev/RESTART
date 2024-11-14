import time
import random
name = input("Hello what is your name? ")
print("Hello " + name + " my name is Jupii.")
time.sleep(1)

Yes = "Yes"
No = "No"
yes = "yes"
no = "no"

game_prompt = input("Would you like to play a game of guess the number?\nYes or No\n")
if game_prompt == Yes or yes:
    print("Great! I'll go first")
    time.sleep(0.7)
    print("Goodluck!")
    time.sleep(0.7)
    def guess_game():
        number_to_guess = random.randint(0, 50)
        guess = None
        max_attempts = 5
        attempts = 0
        while guess != number_to_guess and attempts < max_attempts:
            guess = int(input("Enter a number between 0-50:\n"))
            attempts += 1
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print("Congrats you guessed the correct number!")

        if guess != number_to_guess:
            print(f"OPPS! Seems like you've used up all you {max_attempts} attempts.\nThe correct number was {number_to_guess}.")
            time.sleep(0.7)
    def main():
        while True:
            guess_game()
            play_again = input("Would you like to try again?\nYes or No\n")
            if play_again != "Yes" or "yes":
                print("Thank you for playing.")
            elif play_again == "No" or "no":
                print("Okay! Goodbye.")
            else:
                print("Please enter a valid option.")
                break
    main()
elif game_prompt == No or no:
    print("Hmmm!\n You're no fun.")
else:
    print("You entered an invalid option.")


    


        