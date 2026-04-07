

text = input('What is your message: \n')
shift = int(input('How far would you like to shift your message:(1-26) '))

def ceaser_cipher(text,shift):
    result = ''
    for char in text:
        if char.isalpha():
            char_as_unicode = ord(char)
            if char_as_unicode >= ord('a') and char_as_unicode <= ord('z'):
                base = ord('a')
            elif char_as_unicode >= ord('A') and char_as_unicode <=ord ('Z'):
                base = ord('A')
            char_as_unicode -= base
            char_as_unicode += shift
            char_as_unicode = char_as_unicode % 26
            char_as_unicode += base
            shifted_char = chr(char_as_unicode)
            result += shifted_char

        else:
            result += char
    return result
def decode_cipher(message,shift):
    if shift > 0:
        shift = -shift
        decode_message = ceaser_cipher(message,shift)
    else:
        shift = shift * -1
        decode_message = ceaser_cipher(message,shift)
    return decode_message
message=ceaser_cipher(text,shift)   
print(message)
with open('my_message.txt','w') as file:
    file.write(ceaser_cipher(text,shift))
with open('my_decoded_message.txt','w')as file:
    file.write(decode_cipher(message,shift))
user_input = input('Would you like to decode your message.:(y,n) ')
if user_input == 'y':
    print(decode_cipher(message,shift))
else:
    print('Have a nice day.')