user_operation = input('What would you like to do:(add, subtract, multiply, divide, remainder, expnonents, exit )\n')
user_number = 0
def add_operation():
    answer = 0
    user_number=int(input('Please enter a number:(enter 0 to exit) '))
    with open ('calculator_log.txt','a') as file:
         file.write(f'{user_number} + ')
    while user_number != 0:
        answer += user_number
        user_number=int(input('Please enter a number: (enter 0 to exit)'))   
        if user_number != 0:
                with open ('calculator_log.txt','a') as file:
                    file.write(f'{user_number} + ')
        else:
                with open ('calculator_log.txt','a') as file:
                    file.write(F' = {answer}')
    return answer
    return answer(user_number)
def subtract_operation():
    answer = 0
    user_number=int(input('Please enter a number:(enter 0 to exit) '))
    with open ('calculator_log.txt','a') as file:
        file.write(f'{user_number} - ')
    while user_number != 0:
        answer -= user_number
        user_number=int(input('Please enter a number: (enter 0 to exit)'))
        if user_number != 0:
                with open ('calculator_log.txt','a') as file:
                    file.write(f'{user_number} - ')
        else:
                with open ('calculator_log.txt','a') as file:
                    file.write(F' = {answer}')
    return answer
def multiply_operation():
    first_number = int(input('please enter a number: '))
    second_number = int(input('please enter a number: '))
    answer = first_number * second_number
    with open ('calculator_log.txt','a') as file:
         file.write(f'{first_number} * {second_number} = {answer}')
    return answer
def divide_operation():
    first_number = int(input('please enter a number: '))
    second_number = int(input('please enter a number:'))
    answer = first_number/second_number
    with open ('calculator_log.txt','a') as file:
         file.write(f'{first_number} / {second_number} = {answer}')
    return answer
def remainder_operation():
    first_number = int(input('please enter a number: '))
    second_number = int(input('please enter a number: '))
    answer = first_number % second_number
    with open ('calculator_log.txt','a') as file:
         file.write(f'{first_number} % {second_number} = {answer}')
    return answer
def exponents_operation():
    first_number = int(input('please enter a number: '))
    second_number = int(input('what is the exponent you would like to multiply by: '))
    answer = first_number ** second_number
    with open ('calculator_log.txt','a') as file:
         file.write(f'{first_number} ^ {second_number} = {answer}')
    return answer
while user_operation != exit:
    if user_operation == 'add':
        print(add_operation())
        user_operation = input('What would you like to do:(add, subtract, multiply, divide, remainder, expnonents, exit )\n')
    elif user_operation == 'subtract':
        print(subtract_operation())
        user_operation = input('What would you like to do:(add, subtract, multiply, divide, remainder, expnonents, exit )\n')
    elif user_operation == 'multiply':
        print(multiply_operation())
        user_operation = input('What would you like to do:(add, subtract, multiply, divide, remainder, expnonents, exit )\n')
    elif user_operation == 'divide':
        print(divide_operation())
        user_operation = input('What would you like to do:(add, subtract, multiply, divide, remainder, expnonents, exit )\n')
    elif user_operation == 'remainder':
        print(remainder_operation())
        user_operation = input('What would you like to do:(add, subtract, multiply, divide, remainder, expnonents, exit )\n')
    elif user_operation == 'exponents':
        print(exponents_operation())
        user_operation = input('What would you like to do:(add, subtract, multiply, divide, remainder, expnonents, exit )\n')
    else:
        break


print('Have a nice day')