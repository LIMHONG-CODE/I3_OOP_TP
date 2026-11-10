class LuckyNumberGame:
    def __init__(self, number):
        # store the number provided by the user
        self.number = number

    def get_next_number(self):
        # Return the integer immediately after the stored number.
        return self.number + 1


def ask_to_play_again():
    # Keep asking until the user enters a valid yes-or-no answer.
    while True:
        answer = input("Do you want to play again? (Yes/No): ").strip().lower()

        if answer in {"yes", "no"}:
            return answer == "yes"
        
        print("Please enter yes or no.")

def main():
    # Run another round until the user chooses to stop .
    while True:
        try:
            # Convert the user's input to an integer for the game.
            number = int(input("Please enter an integer: "))

        except ValueError:
            # A non-integer input is rejected; the loop will prompt again.
            print("Please enter a valid integer.")

        else:
            # Create the game and display the next integer.
            game = LuckyNumberGame(number)
            print(f"The next number is: {game.get_next_number()}")
            
        # ask the user if they want to play again but if they say no, break the loop and end the game
        if not ask_to_play_again():
            # stop loop
            break

# Start the game only when this file is run directly.
if __name__ == "__main__":
    main()
