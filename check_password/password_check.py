
user_name = input('Please enter your user name:')
print('password must include at least \n One capital letter \n one lowercase letter \n one number\n one special character\n  at least 8 characters')
user_password = input('Please enter your password: ')
password_confirmation = input('Please re-enter your password: ')
def password_length (user_password):
    length = 0
    for letter in user_password:
        length += 1
    if length >= 8:
        return 
    else:
        return False
def character_is_capital(user_password):
    capital_string = ''
    answer = bool
    for letter in user_password:
        uniletter = ord(letter)
        if uniletter >= ord('A') and uniletter <= ord('Z'):
            capital_string += letter
        if capital_string != '':
            answer = True
        elif capital_string == '':
            answer = False
    return answer
def character_is_lowercase(user_password):
    answer = bool
    capital_string = ''
    for letter in user_password:
        uniletter = ord(letter)
        if uniletter >= ord('a') and uniletter <= ord('z'):
            capital_string += letter
        if capital_string != '':
            answer = True
        elif capital_string == '':
            answer = False
    return answer
def character_is_numeric(user_password):
    for letter in user_password:
        if letter.isnumeric():
            answer = True
        else:
            answer = False
    return answer
def character_is_special_character(user_password):
    special_character_list = ''
    answer = bool
    for letter in user_password:
        uniletter = ord(letter)
        if uniletter < ord ('a') or uniletter > ord('A'):
            special_character_list += letter   
    if special_character_list != '':
        answer = True
    else:
        answer = False
    return answer       
capital_letter = character_is_capital(user_password)
lowercase_letter = character_is_lowercase(user_password)
number = character_is_numeric(user_password) 
special_character = character_is_special_character(user_password)
correct_password = False
print(character_is_capital(user_password))
print(character_is_lowercase(user_password))
print(character_is_numeric(user_password))
print(character_is_special_character(user_password))
while correct_password != True:
    if user_password == password_confirmation:
        if capital_letter == True and lowercase_letter == True and number == True and special_character == True:
            print('Thank You.')
            correct_password = True
        elif capital_letter ==True and number == True and special_character == True:
            print('Please include at least one lowercase letter')
            user_name = input('Please enter a password: ')
            password_confirmation = input('Please re-enter your password: ')
        elif number == True and lowercase_letter == True and special_character == True:
            print('Please enter at least one capital letter:.')
            user_name = input('Please enter a password: ')
            password_confirmation = input('Please re-enter your password: ')
        elif capital_letter == True and lowercase_letter == True and special_character == True:
            print('Please include at least one number.')
            user_name = input('Please enter a password: ')
            password_confirmation = input('Please re-enter your password: ') 
        elif capital_letter == True and  number == True and lowercase_letter == True:
            print('Please include at least one special character.')  
            user_name = input('Please enter a password: ')
            password_confirmation = input('Please re-enter your password: ')
    else:
        print ('Your passwords do not match.')
        user_name = input('Please enter a password: ')
        password_confirmation = input('Please re-enter your password: ')
with open ('password_log.txt','a') as file:
    file.write(f'{user_name} : {user_password}\n')  
    
