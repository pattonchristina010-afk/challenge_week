user_number = int(input('Please enter your number: '))
check_range = user_number + 1
def check_for_Prime(check_range,user_number):
    answer = True
    for num in range (2,check_range):
        if user_number <= 2:
            answer = False
        elif num == user_number:
            answer = True
        elif user_number % num == 0:
                answer = False
        else:
            continue
        return answer
def create_prime_list(check_range):
    for num in range(1,check_range):
        my_prime = check_for_Prime(check_range,num)
        if my_prime == True:
           with open('prime_list.txt','a')as file:
                file.write(f'{num}, ')
        else:
            continue

user_choice = input('What would you like to do:\n1. list prime numbers up to your number\n2. find out if your number is a prime number\n(1,2): ')
if user_choice == '1':
    with open('prime_list.txt','w')as file:
        file.write(f'Prime numbers up to {user_number} are."\n')
    create_prime_list(check_range)
    with open('prime_list.txt','r')as file:
        for line in file:
          print(file.readline())
elif user_choice == '2':
    is_prime =  check_for_Prime(check_range,user_number)
    if is_prime == True:
        print(f"{user_number} is a prime number")
    else:
        print(f'{user_number} is not a prime number')


