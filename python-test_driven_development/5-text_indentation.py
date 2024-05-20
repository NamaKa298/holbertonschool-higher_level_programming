#!/usr/bin/python3
'''4. Text indentation'''


def text_indentation(text):
    '''function that prints a text with 2 new lines after each
    of these characters: ., ? and :'''
    k = ['.', '?', ':']
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] in k:
            print(text[i], end='\n')
            print()
        elif (text[i-1] in k or text[i-1] == ' ') and text[i] == ' ':
            pass
        else:
            print(text[i], end='')
