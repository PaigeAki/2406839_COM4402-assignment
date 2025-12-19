# write comment here
user_score = 0
total_question_score = 0
question_counter = 0
i = 0
# write commwnt here
questions_list = [
    {
        'question_text': 'Question 1: what colour is the sky',
        'answers' : ['1. blue', '2. red', '3. green', '4. yellow'],
        'correct_answer' : '1',
        #'value': 2,
    },
    {
        'question_text': 'Question 2: what shape is a square',
        'answers' : ['1. circle', '2. square', '3. triangle', '4. rectangle'],
        'correct_answer' : '2',
        #'value': 2,
    },
    {
        'question_text': 'Question 3: what is 2+2',
        'answers' : ['1. 5', '2. 4', '3. 3', '4. 7'],
        'correct_answer' : '2',
        #'value': 2,
    },
    {
        'question_text': 'Question 4: what is 3+4 ',
        'answers' : ['1. 5', '2. 4', '3. 3', '4. 7'],
        'correct_answer' : '4',
        #'value': 2,
    },
    {
        'question_text': 'Question 5: what is 2+1',
        'answers' : ['1. 5', '2. 4', '3. 3', '4. 7'],
        'correct_answer' : '3',
        #'value': 2,
    }
]
# write commment here
for question in questions_list:
    test_ans = False
    total_question_score = total_question_score +1
    #num = random.randint(0,len('answers')-1)
    print(question['question_text'])
    for answer in question['answers']:
        print(answer)

    # while loop to check that the user has entered a valid answer
    while test_ans == False :
        user_input = str(input('Enter your answer (1-4): ')).strip()
        #test_ans = int(user_input)
        if user_input.isdigit() == True and int(user_input) >= 1 and int(user_input) <= 4:
            test_ans = True
        else:
            print('Please enter a number option for the question (1-4)')
            test_ans = False

    # check for correct answer using switch statment
    match user_input:
        case u if u == question['correct_answer']:
            user_score = user_score + 1
            print('Correct!')
        case _:
            print('Incorrect :(')
    # same thing but if
    # if user_input == question['correct_answer']:
    #     user_score += 1
    #     print('Correct!')
    # else:
    #     print('Incorrect :(')

# displays the test is over and the scores
print("quiz complete")
print("your score is: ", user_score)
print("total question score: ", user_score, "out of", total_question_score)
print("that's", user_score/ total_question_score *100, "%")
print("thanks for participating")

