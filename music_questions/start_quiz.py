import os
import subprocess

def play_game():
    # Execute the music_questions program to play 10 questions
    print("Welcome to the music quiz!")
    try:
        subprocess.run(['python', 'music_question.py'])
    except FileNotFoundError:
        print("Error: music_questions.py not found. Make sure it exists in the current directory.")
        return

    # Ask the player if they want to continue playing
    play_again = input("Do you want to play another round? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        return

    # Execute the generate_music_questions program to generate another set of 10 questions
    try:
        subprocess.run(['python', 'generate_music_questions.py'])
    except FileNotFoundError:
        print("Error: generate_music_questions.py not found. Make sure it exists in the current directory.")
        return

    # Restart the game
    play_game()

if __name__ == "__main__":
    play_game()
