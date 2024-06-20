# an application to collect consumers' data on our new product BRAINY
import time
from tracemalloc import stop
question_number = 0
right = 0
wrong = 0
name = str(input('Enter your name'))
time.sleep (0.5)
print(f'Welcome {name}! \n We will be taking you through some survey questions on our new product BRAINY, please take your time to answer carefully. \n Thanks!')
time.sleep (4)

def question_one():
    global right, wrong, question_number
    print('What is the name of the organization that introduced BRAINY?')
    time.sleep(0.5)
    print('A. NUPAT', 'B. NUTECH', 'C. NUPART', 'D. NIPAT')
    answer = str(input())
    if answer == 'A' or answer == 'a' or answer == 'NUPAT' or answer == 'Nupat' or answer == 'nupat':
        print("That's correct!")
        right += 5
    else:
        print("That's wrong!")
        wrong += 1
    question_number += 1
question_one()
time.sleep(1)
print(f"Hello {name}, You've got {right} points. Congrats, on to the next question")
print()
time.sleep(4)


def question_two():
    global right, wrong, question_number
    print('BRAINY is what kind of software?')
    time.sleep(0.5)
    print('A. GAMING', 'B. WEB-DEVELOPMENT', 'C. GRAPHICS', 'D. AI')
    answer = str(input())
    if answer == 'D' or answer == 'd' or answer == 'AI' or answer == 'Ai' or answer == 'ai':
        print("That's correct!")
        right += 5
    else:
        print("That's wrong!")
        wrong += 1
    question_number += 1
question_two()
time.sleep(1)
print(f"Hello {name}, You've got {right} points. Congrats, on to the next question")
print()
time.sleep(4)


def question_three():
    global right, wrong, question_number
    print('BRAINY is a _______ AI software?')
    time.sleep(0.5)
    print('A. FAST', 'B. ROBOTIC', 'C. SWIFT', 'D. JET')
    answer = str(input())
    if answer == 'B' or answer == 'b' or answer == 'ROBOTIC' or answer == 'Robotic' or answer == 'robotic':
        print("That's correct!")
        right += 5
    else:
        print("That's wrong!")
        wrong += 1
    question_number += 1
question_three()
time.sleep(1)
print(f"Hello {name}, You've got {right} points. Congrats, on to the next question")
print()
time.sleep(4)


def question_four():
    global right, wrong, question_number
    print('BRAINY supports the following except?')
    time.sleep(0.5)
    print('A. CAR', 'B. BICYCLE', 'C. COMPUTER', 'D. PHONE')
    answer = str(input())
    if answer == 'B' or answer == 'b' or answer == 'BICYCLE' or answer == 'Bicycle' or answer == 'bicycle':
        print("That's correct!")
        right += 5
    else:
        print("That's wrong!")
        wrong += 1
    question_number += 1
question_four()
time.sleep(1)
print(f"Hello {name}, You've got {right} points. Congrats, on to the next question")
print()
time.sleep(4)


def question_five():
    global right, wrong, question_number
    print('Can BRAINY work in humans?')
    time.sleep(0.5)
    print('A. YES', 'B. MAYBE', 'C. NO', 'D. NO IDEA')
    answer = str(input())
    if answer == 'C' or answer == 'c' or answer == 'NO' or answer == 'No' or answer == 'no':
        print("That's correct!")
        right += 5
    else:
        print("That's wrong!")
        wrong += 1
    question_number += 1
question_five()
time.sleep(2)
if right <= 15:
    print(f'Oooops, you got {right} points in total. \n Would you like to take the survey again?')
    print('YES' ' ' 'NO')
    response = str(input())
    if response == 'YES' or response == 'Yes' or response == 'yes':
        question_one()
        question_two()
        question_three()
        question_four()
        question_five()
        print(f'{name}, Thank you for taking this survey.')
        stop
        if right <= 15:
            print(f'Oooops, you got {right} points in total. \n Would you like to take the survey again?')
            print('YES'  'NO')
            response = str(input())
            if response == 'YES' or response == 'Yes' or response == 'yes':
                question_one()
                question_two()
                question_three()
                question_four()
                question_five()
                print(f'{name}, Thank you for taking this survey.')
                stop
    else:
        print(f"Congratulations {name}, you got {right} points in total. \n Thank you for taking this survey.")
if right > 15:
    print(f"Congratulations {name}, you got {right} points in total. \n Thank you for taking this survey.")
print()
