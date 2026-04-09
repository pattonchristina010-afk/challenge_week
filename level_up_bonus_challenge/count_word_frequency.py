import string
import json
with open ('my_file.txt','r') as file:
    text = file.read()
word_list = {}
translator = str.maketrans('','',string.punctuation)
cleaned_text = text.lower().translate(translator)
cleaned_text = cleaned_text.split()
print (cleaned_text)
def word_count(cleaned_text):
    for word in cleaned_text:
        my_word = word
        my_count = 0
        for word in cleaned_text:
            if word == my_word:
                my_count += 1
            else:
                continue
        word_list.update({my_word:my_count})
    return word_list
current_dictionary = word_count(cleaned_text)
sorted_list = dict(current_dictionary.items(),key=lambda item: item[1], reverse = True)
print (word_count(cleaned_text))
print (sorted_list)
with open ('my_dictionary.json','w') as file:
    json.dump(sorted_list,file)