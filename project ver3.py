# remember to put every thing into functions (read the assignment breif)

# initialising variables
user_score = 0
total_question_score = 0
question_counter = 0
i = 0
# write comment here
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

def run_quizz(questions_list, total_question_score, user_score):
    # displays the question and the multiple choice answers
    for question in questions_list:
        test_ans = False
        total_question_score = total_question_score +1
        # usine \n to make a empty line before each question to help readability
        print("\n" + question['question_text'])
        for answer in question['answers']:
            print(answer)

        # while loop to check that the user has entered a valid answer
        while test_ans == False :
            user_input = str(input('Enter your answer (1-4): ')).strip()
            if user_input.isdigit() == True and int(user_input) >= 1 and int(user_input) <= 4:
                test_ans = True
            else:
                print('Please enter a number option for the question (1-4)')
                test_ans = False
        # a function to check the answer
        user_score = check_answer(user_input, question, user_score)
    return user_input, total_question_score, user_score


def check_answer(user_input, question, user_score):
    # check for correct answer using switch statment
    match user_input:
        case u if u == question['correct_answer']:
            user_score = user_score + 1
            print('Correct!')
        case _:
            print('Incorrect :(')
    return user_score


# calls the function that runs the quiz and gets 3 variables returned
user_input, total_question_score,  user_score= run_quizz(questions_list, total_question_score, user_score)

# displays the test is over and the scores
# putting in an extra print command so the results separate from the answers to help readability
print()
print("quiz complete")
print("your score is: ", user_score)
print("total question score: ", user_score, "out of", total_question_score)
print("that's", user_score/ total_question_score *100, "%")
print("thanks for participating")