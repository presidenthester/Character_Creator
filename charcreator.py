melee = 0
health = 0
stamina = 0
weight = 0
ranged = 0





name = input("What is your name?")

first_question = {
    "question_1": "What happened tonight"
         }

first_question_answers = {
    "answer_1": "Car accident",
    "answer_2": "Muggged",
    "answer_3": "Construction accident",
}

print(first_question["question_1"] + f" {name}?\nA: {first_question_answers['answer_1']}\nB: {first_question_answers['answer_2']}\nC: {first_question_answers['answer_3']}\n")

ques_1_answer = input("Response")

if ques_1_answer == '':
    print(f"{name}! You need to tell me what happened!")
    print(ques_1_answer)

elif ques_1_answer == first_question_answers["answer_1"].lower():
    print(f"Ok {name} a {first_question_answers['answer_1']} ")

