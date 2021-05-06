def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print(f'What a great name you have, {name}!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    age = (int(input()) * 70 + int(input()) * 21 + int(input()) * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')
    for i in range(0, int(input())+1):
        print(i, "!")


def test():
    print("Let's test your programming knowledge.")
    print(r"""Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.""")
    while int(input()) != 2:
        print("Please, try again.")
        continue
    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Arthur', '2021')
remind_name()
guess_age()
count()
test()
end()
