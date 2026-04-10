user_rule = int(input('what would you like to divide by: '))
user_tag = input('what would you like to change the numbers to: ')
print_option = ('Would you like to create a file with your list:(y,n) ')

                
def fizz_bang(user_rule, user_tag):
    for num in range(1,101):
        number_list=[]
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
            number_list +='FizzBuzz'
        elif num % 3 == 0:
            print('Fizz')
            number_list +='Fizz'
        elif num % 5 == 0:
            print('Buzz')
            number_list+='Buzz'
        elif num % 7 == 0:
            print('Bang')
        elif num % user_rule == 0:
            print(user_tag)
            number_list += user_tag
        else:
            print(num)
            converted_num = str(num)
            number_list += converted_num
    print(number_list)
    result = ' '.join(number_list)
    return result
user_choice = input('Would you like to save your list?(y,n) ')
if user_choice == 'y':
    with open ('mylist.txt','a') as file:
        file.write(f'{fizz_bang(user_rule,user_tag)}\n')
    print('Your list has been saved to mylist.txt have a nice day.')
else:
    print('Have a nice day.')
