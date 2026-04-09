import time
def get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

user_message = input('What would you like to enter into the log: \n')
current_time = get_time()
log_entry = (f'{user_message} {current_time}')
with open ('log.txt','a') as file:
    file.write(log_entry)