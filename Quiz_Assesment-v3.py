# mathematical based quiz, loops, input and output,
# conditions, data collection(list and percentage of right answers)
# asks the user for game limits(can be set rounds if extra time)

# Basic Facts Quiz

# (done)	Allow users to choose the numbers being used / the level of the questions being asked.
# (done) -	Allow users to choose the operation involved.
#  -	Allow users to choose a quiz where the answers to subtraction questions are always positive.
# Generate division questions where the answers are always integers.
# user inputs two problem types
# asks user if they want quiz history


import random


# Checks if question response is an integer
def int_check(question):
    while True:

        flag = True

        try:
            int_response = int(input(question))

        except ValueError:
            flag = False
        if flag:
            return int_response
        else:
            print("Please enter an integer")


# Checks if question response is a appropriate problem type
def prob_check(question):
    while True:
        pattern = input(question)

        if '+' in pattern:
            oa = '+'
            return oa
        elif '-' in pattern:
            oa = '-'
            return oa
        elif '*' in pattern:
            oa = '*'
            return oa
        elif '/' in pattern:
            oa = '/'
            return oa
        else:
            print("please enter a problem type")


# Checks if question response is either considered a "yes" or "no"
def yes_no(question):
    while True:
        response = input(question).lower()

        # check user response, question
        # repeat if users don't enter yes/no
        if response == "yes" or response == "y" or response == "":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes/no")


# Player instructions
def instructions():
    print('''

You will be asked for a problem type that will be used for the quizz
* can not choose two simultaneously
* Division is rounded down from 0.6!

Enter the number parameter for your quizz
* must be an integer

Questions will be asked depending on your previous answers

'enter' is considered 'yes'


    ''')


# Main routine


(print("Welcome to the Quizzz"))
# Asks user if they want instructions for the run
want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
    instructions()
while True:
    # Asks for the problem type the user wants to use for the run
    op = prob_check('Enter the problem type, +, -, *, /, : ')

    # Stores the max & min number the user inputs to use for random generation
    MaxNum = (int_check('Enter max barrier: '))
    MinNum = (int_check('Enter min barrier: '))
    # Base-Scores
    wrongs = 0
    rights = 0
    game_history = []

    while True:
        # Generates two random number inbetween the users chosen max & min number
        a = random.randint(MinNum, MaxNum)
        b = random.randint(MinNum, MaxNum)
        # Gives biggest number generated on the left of the equation for division and minus
        # Recognises the problem type given & does the math - gives result
        if op in ['-', '/']:
            a, b = max(a, b), min(a, b)
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            result = a // b
        # Prints Equation for user & takes users input/answer
        equation = '' + ' '.join([str(a), op, str(b), '= '])
        answer = int_check(equation)
        history_item = f"{equation}{result}"
        game_history.append(history_item)
        # Checks if user input = results & adding one point to the appropriate scoring
        if int(answer) == result:
            rights += 1
            print("Right!")
        else:

            wrongs += 1
            print("Wrong!")
            print(f"Answer was {result}")
        # Asks if user wants to play again, if "n" score is shown and breaks
        again = yes_no('Again? ')
        if again == "no":
            score = str(rights) + ' right, ' + str(wrongs) + ' wrong.'
            print('\nYour score:', score)

            want_history = yes_no("Do you Want your Game history? ")
            if want_history == "yes":
                for item in game_history:
                    print(item)
            break