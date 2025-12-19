score = 0
total = 0
question_counter = 0
i = 0
questions = [
    {
        'question_text': 'Question 1: what colour is the sky',
        'answers' : ['1. blue', '2. red', '3. green', '4. yellow'],
        'correct_answer' : '1',
    },
    {
        'question_text': 'Question 2: what shape is a square',
        'answers' : ['1. circle', '2. square', '3. triangle', '4. rectangle'],
        'correct_answer' : '2',
    },
    {
        'question_text': 'Question 3: what is 2+2',
        'answers' : ['1. 5', '2. 4', '3. 3', '4. 7'],
        'correct_answer' : '2',
    },
]

for qu in questions:
    # select_question  = random.choice(qu['question'])
    print(qu['question'])

    for answer in qu['answers']:
        print(answer)

    userInput = input('enter answer here: ')
    if userInput == qu['correct_answer']:
        score = score + 1
    total = total + 1
print('your score is', score, ' out of ', total)
print('quiz complete')