import json
import os
import random

def generate_questions(num_questions, music_key_folder):
    questions = []
    music_keys = os.listdir(music_key_folder)

    for _ in range(num_questions):
        question = {}
        question['question'] = "What is the key of this music?"
        question['choices'] = random.sample(["A", "B", "C", "D", "E", "F", "G"], 4)
        question['answer'] = random.choice(question['choices'])
        question['music_key'] = random.choice(music_keys)
        questions.append(question)

    return questions

def save_questions(questions, file_path):
    with open(file_path, 'w') as file:
        json.dump(questions, file, indent=2)

if __name__ == "__main__":
    num_questions = 10
    music_key_folder = 'D:\Program Files\music_keys'  # Folder containing music key files
    output_file = 'D:\Program Files\music_questions\music_questions.json'  # Output file name

    questions = generate_questions(num_questions, music_key_folder)
    save_questions(questions, output_file)

    print(f"{num_questions} random music questions generated and saved to {output_file}.")

