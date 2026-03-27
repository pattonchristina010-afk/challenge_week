user_list=[]
user_answer = input('Would you like to enter a number:(y,n) ')
while user_answer == 'y':
    user_list.append(int(input('Please enter a number: ')))
    user_answer = input('Would you like to enter a number:(y,n) ')
    continue
print(user_list)
max_num = -10000000
def find_max (user_list,max_num):
    for num in user_list:
        if num > max_num:
            max_num = num
        else:
            continue
    return max_num
def find_index(user_list):
    for index, value in enumerate(user_list):
        if value == find_max(user_list,max_num):
            return index
        else:
            continue
if user_list != []:
    print(f'The largest number in your list is: {find_max(user_list,max_num)}\n its index is {find_index(user_list)}')
else:
    print('Your list is empty')