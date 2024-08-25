import json

with open('questions.json', 'r') as file:
    content = file.read()

quiz_data = json.loads(content)

for question in quiz_data:
    print(question["question_text"])
    for index, option in enumerate(question["options"]):
        print(f"{index+1} - {option}")
    user_choice = int(input("Mark your nswer:"))
    question["user_answer"] = user_choice

score = 0
for index, question in enumerate(quiz_data):
    if question["user_answer"] == question["correct_answer"]:
        score = score + 1
        answer_type = "Your answer is correct!"
    else:
        answer_type = "Your answer is wrong." 
    message = f"{index+1} - {answer_type}, Correct answer: {question['correct_answer']}, Your Anser: {question['user_answer']}"
    print(message)

print (f"Result - {score}/{len(quiz_data)}")