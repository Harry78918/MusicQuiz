import json
import os
import random

def generate_questions(num_questions, music_key_folder):
    questions = []

    music_keys = [os.path.splitext(file)[0] for file in os.listdir(music_key_folder)]
    for _ in range(num_questions):
        question = {}
        question['question'] = "What is the key of this music?"
        
        # Select a random music key as the answer
        answer = random.choice(music_keys)
        
        # Choose three random choices, including the answer
        choices = [answer]
        while len(choices) < 4:
            random_choice = random.choice(music_keys)
            if random_choice not in choices:
                choices.append(random_choice)
        
        # Shuffle the choices to ensure the answer is not always in the same position
        random.shuffle(choices)
        
        question['choices'] = choices
        question['answer'] = answer
        question['music_key'] = answer + ".mp3"
        
        questions.append(question)

    return questions

def save_questions(questions, file_path):
    with open(file_path, 'w') as file:
        json.dump(questions, file, indent=2)

def generate_questions_and_save(num_questions, music_key_folder, output_file):
    questions = generate_questions(num_questions, music_key_folder)
    save_questions(questions, output_file)

if __name__ == "__main__":
    num_questions = 10
    music_key_folder = 'D:\Program Files\music_keys'  # Folder containing music key files
    output_file = 'D:\Program Files\music_questions\music_questions.json'  # Output file name

    generate_questions_and_save(num_questions, music_key_folder, output_file)
