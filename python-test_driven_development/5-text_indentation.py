#!/usr/bin/python3
'''4. Text indentation'''


def text_indentation(text):
    '''function that prints a text with 2 new lines after each
    of these characters: ., ? and :'''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i], end='\n')
            print()
        elif (text[i-1] == '.' or text[i-1] == '?' or text[i-1] == ':' or //
              text[i-1] == ' ') and text[i] == ' ':
            pass
        else:
            print(text[i], end='')
