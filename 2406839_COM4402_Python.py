# initialising variables
user_score = 0
total_question_score = 0
i = 0
# list of dictionaries for storing the questions, answers and multiple choice options, each question is worth one mark
questions_list = [
    {
        'question_text': 'Question 1: what colour is the sky',
        'answers': ['1. blue', '2. red', '3. green', '4. yellow'],
        'correct_answer': '1',
    },
    {
        'question_text': 'Question 2: what shape is a square',
        'answers': ['1. circle', '2. square', '3. triangle', '4. rectangle'],
        'correct_answer': '2',
    },
    {
        'question_text': 'Question 2: what shape is a circle',
        'answers': ['1. circle', '2. square', '3. triangle', '4. rectangle'],
        'correct_answer': '1',
    },
    {
        'question_text': 'Question 3: what is 2+2',
        'answers': ['1. 5', '2. 4', '3. 3', '4. 7'],
        'correct_answer': '2',
    },
    {
        'question_text': 'Question 4: what is 3+4 ',
        'answers': ['1. 5', '2. 4', '3. 3', '4. 7'],
        'correct_answer': '4',
    },
    {
        'question_text': 'Question 5: what is 2+1',
        'answers': ['1. 5', '2. 4', '3. 3', '4. 7'],
        'correct_answer': '3',
    }
]
print("\nWelcome to the Holton College Quiz!\nPlease answer with the number (1, 2, 3, or 4) of your choice.")

def run_quiz(questions_list, user_quiz_score):
    # displays the question and the multiple choice answers
    for question in questions_list:
        valid_user_answer = False
        # usine \n to make a empty line before each question to help readability
        print("\n" + question['question_text'])
        for answer in question['answers']:
            print(answer)

        # while loop to check that the user has entered a valid answer that repeats until it is
        while valid_user_answer == False:
            user_input = str(input('Enter your answer (1-4): ')).strip()
            if (user_input.isdigit() == True) and (1<= int(user_input) <= 4):
                valid_user_answer = True
            else:
                print('Please enter a number option for the question (1-4)')
                valid_user_answer = False
        # a function to check the answer
        user_quiz_score = check_answer(user_input, question, user_quiz_score)
    return user_input, user_quiz_score


def check_answer(user_input, question, user_quiz_score):
    # check for correct answer using switch statment, change to if
    if user_input == question['correct_answer']:
        user_quiz_score = user_quiz_score + 1
        print('Correct! :)')
    else:
        print('Incorrect :(')
    return user_quiz_score


# calls the function that runs the quiz and gets 3 variables returned
user_input, user_score = run_quiz(questions_list, user_score)

# displays the test is over and the scores
# putting in an extra print command so the results separate from the answers to help readability
print()
print("quiz complete")
print("your score is: ", user_score)
print("total question score: ", user_score, "out of", len(questions_list))
print("that's", user_score / len(questions_list) * 100, "%")
print("thanks for participating")