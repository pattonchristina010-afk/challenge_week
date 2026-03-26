import re
user_phrase = input('Please enter the word or phrase you want to check: ')
def is_palindrome(user_phrase):
    normal_phrase = re.sub(r'[^A-Za-z0-9]', '', user_phrase)
    reveres_phrase = normal_phrase[::-1]
    if normal_phrase == reveres_phrase:
        return 'Yes it is a palindrome'
    else:
        return 'This is not a palindrome'
print(is_palindrome(user_phrase))   