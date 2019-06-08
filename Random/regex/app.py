#!/usr/bin/env python3

import re
import sys

def transform_text(data):
    text = "" # will hold transformed text
    pattern = r'(^\w)|([!,.:;?]\s\w)'

    with open(data) as f:
        for line in f:
            text += re.sub(pattern, pretty, line)
    # save text to a new file -- TODO: I should do this in a more Pythonic way
    f = open('modified_text.txt', 'w')
    f.write(text)
    f.close()

def pretty(match):
    return match.group().replace(' ', '').lower()

def manual():
    """Displays a HOW_TO guide."""
    print('\nUsage: python3 app.py {YOUR_.TXT_FILE}\n\n-- You need to pass an argument.\n')

if __name__ == '__main__':
    # get command line argument
    try:
        if len(sys.argv) > 1:
            transform_text(sys.argv[1])
        else:
            manual()
    except ValueError as e:
        print(f'An exception occurred - {e}')

