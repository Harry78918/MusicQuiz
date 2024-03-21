import json
import random
import os
import pygame

def load_questions(file_path):
    with open(file_path, 'r') as file:
        questions = json.load(file)
    return questions

def play_music(music_key):
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join('D:\Program Files\music_keys', music_key))
    pygame.mixer.music.play()
    pygame.time.wait(2000)  # Adjust the wait time according to your music length

def play_quiz(questions):
    score = 0
    question_count = 0
    pygame.init()
    while question_count < 10:
        question = random.choice(questions)
        music_key = question['music_key']
        play_music(music_key)

        print("\nQuestion:", question['question'])
        print("Choices:")
        for idx, choice in enumerate(question['choices']):
            print(f"{idx+1}. {choice}")
        
        player_choice = input("Enter your choice (1, 2, 3, ...): ")
        if player_choice.isdigit():
            player_choice = int(player_choice)
            if 1 <= player_choice <= len(question['choices']):
                if question['choices'][player_choice-1] == question['answer']:
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect! The correct answer is:", question['answer'])
                    score -= 1
            else:
                print("Invalid choice! Please enter a number between 1 and", len(question['choices']))
        else:
            print("Invalid input! Please enter a number.")

        print("Your score:", score)

        question_count += 1
        if question_count == 10:
            print("You've completed 10 questions!")
            break

        play_again = input("Do you want to play another round? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thanks for playing!")
            pygame.mixer.quit()
            break

if __name__ == "__main__":
    file_path = 'D:\Program Files\music_questions\music_questions.json'  # Path to your JSON file
    questions = load_questions(file_path)
    play_quiz(questions)
