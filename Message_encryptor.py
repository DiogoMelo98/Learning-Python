# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 19:15:36 2021

@author: diogo
"""

# A-Z 65-90
# a-z 97-122
# ord(your_letter)
# chr(your_code)

# Hints
# Use isupper() to decide which unicodes to work with
# Add the key (number of characters to shift) and if
# the key is bigger or smaller then the unicode for
# A, Z, a, z increase or decrease by 26


# Receive the message to encrypt and the number of
# characters to shift
message = input("Enter your message: ")
key = int(input("How many characters should we shift: "))
# Prepare the secret_message
secret_message = ""
# Cycle through each character in the message
for char in message:
        # If it isn't a letter then keep it as it is
        if char.isalpha():
            # Get the character code and add the shift amount
            char_code = ord(char)
            char_code += key 
            # If uppercase than compare to uppercase unicodes
            if char.isupper():
                # If bigger then Z subtract 26
                if char_code > ord('Z'):
                    char_code -= 26         
                # If smaller than A add 26
                if char_code < ord('A'):
                    char_code += 26            
            # Do the same for lowercase characters
            else:
                if char_code > ord('z'):
                    char_code -= 26             
                if char_code < ord('a'):
                    char_code += 26         
            # Convert from code to letter and add to message
            secret_message += chr(char_code)
# If not a letter leave character as is
        else:
            secret_message += char
print('Encrypted: ', secret_message)

key = -key
orig_message = ''
for char in secret_message:
        # If it isn't a letter then keep it as it is
        if char.isalpha():
            # Get the character code and add the shift amount
            char_code = ord(char)
            char_code += key 
            # If uppercase than compare to uppercase unicodes
            if char.isupper():
                # If bigger then Z subtract 26
                if char_code > ord('Z'):
                    char_code -= 26         
                # If smaller than A add 26
                if char_code < ord('A'):
                    char_code += 26            
            # Do the same for lowercase characters
            else:
                if char_code > ord('z'):
                    char_code -= 26             
                if char_code < ord('a'):
                    char_code += 26         
            # Convert from code to letter and add to message
            orig_message += chr(char_code)
# If not a letter leave character as is
        else:
            orig_message += char
print('Decrypted: ', orig_message)