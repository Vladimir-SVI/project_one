import prompt
import random


def play_even(name):
    print("Answer 'yes' if number even otherwise answer 'no'.")
    count_correct = 0
    while count_correct < 3:
        random_number = random.randint(1, 10)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        result = 'no'
        if random_number % 2 == 0:
            result = 'yes'
        if answer == result:
            print('Correct!')
            count_correct += 1
        else: 
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            break
        if count_correct == 3:
            print(f'Congratulations, {name}!')
