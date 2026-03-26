import re
text = input("please enter a string: ")
cleaned_text=re.sub(r'[^A-Za-z0-9]','',text)
def reverse_string1(cleaned_text):
    reversed_text= cleaned_text[::-1]
    return reversed_text
print(reverse_string1(cleaned_text))
def reverse_string2(cleaned_text):
    result = ''
    for char in cleaned_text:
        result = char + result
    return result
print (reverse_string2(cleaned_text))
if isinstance(text,str):
    print(reverse_string1(cleaned_text))
elif isinstance(text,list):
    reverse_list = text.reverse()
    print(reverse_list)