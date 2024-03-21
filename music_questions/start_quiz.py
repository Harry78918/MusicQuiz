import music_question
import generate_music_questions
import os

def play_game():
    while True:
        file_path = 'music_questions.json'  # Path to the music questions file

        if not os.path.exists(file_path):
            print("Music questions file not found. Generating new questions...")
            generate_music_questions.generate_questions_and_save(num_questions=10, music_key_folder='music_keys', output_file=file_path)

        questions = music_question.load_questions(file_path)
        music_question.play_quiz(questions)

        play_again = input("Do you want to play another round? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
