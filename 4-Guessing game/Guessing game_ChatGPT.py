import random

def guessing_game():
    print("🎉 Welcome to the Guessing Game! 🎉")
    min_attempts = None  # To store the best score across all games

    while True:
        print("\nI am thinking of a number between 1 and 10.")
        target = random.randint(1, 10)
        attempts = 0

        while True:
            try:
                player_choice = int(input("👉 Pick a number (1-10): "))
            except ValueError:
                print("Please enter a valid number!")
                continue

            if player_choice < 1 or player_choice > 10:
                print("Number must be between 1 and 10!")
                continue

            attempts += 1

            if player_choice == target:
                print("🎉 Amazing! You guessed it! Great job! 🎉")
                break
            else:
                # Give hints
                if player_choice < target:
                    print("🔼 Try a higher number!")
                else:
                    print("🔽 Try a lower number!")

        # Update minimum attempts
        if min_attempts is None or attempts < min_attempts:
            min_attempts = attempts

        print(f"\n📊 You got it in {attempts} attempts!")
        print(f"🏆 Your best score (minimum attempts): {min_attempts}")

        # Ask to play again
        play_again = input("\n🔁 Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ("yes", "y"):
            print("\n👋 Thanks for playing! Goodbye!")
            break


# Run the game
guessing_game()
