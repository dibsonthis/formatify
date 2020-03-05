from pynput.keyboard import Key, Controller
import pyperclip
import random
import time

keyboard = Controller()

def get_clipboard_data():
    data = pyperclip.paste()
    time.sleep(0.01)
    return data

def copy_to_clipboard(content):
    pyperclip.copy(content)
    time.sleep(0.01)

def clear_clipboard():
    pyperclip.copy('')

def copy_text():
    keyboard.press(Key.ctrl_l)
    keyboard.press('c')
    keyboard.release(Key.ctrl_l)
    time.sleep(0.01)

def paste_text():
    keyboard.press(Key.ctrl_l)
    keyboard.press('v')
    keyboard.release(Key.ctrl_l)
    time.sleep(0.01)

def delete(string):
    for char in string:
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)

def replace(old, new):
    copy_to_clipboard(new)
    delete(old)
    paste_text()

def split_string(string, ls='\r\n', l='\t', s=' '):
    lines = string.split(ls)
    for line_index, line in enumerate(lines):
        lines[line_index] = line.split(l)
    for line_index, line in enumerate(lines):
        for sentence_index, sentence in enumerate(line):
            line[sentence_index] = sentence.split(s)

    return lines

def join_string(lines, ls='\r\n', l='\t', s=' '):

    for line_index, line in enumerate(lines):
        for sentence_index, sentence in enumerate(line):
            line[sentence_index] = s.join(sentence)
    for line_index, line in enumerate(lines):
        lines[line_index] = l.join(line)

    lines = ls.join(lines)         
    return lines

def make_upper(string):

    lines = split_string(string)

    for line_index, line in enumerate(lines):
        for sentence_index, sentence in enumerate(line):
            for word_index, word in enumerate(sentence):
                sentence[word_index] = word.upper()

    string = join_string(lines)
    return string

def make_lower(string):

    lines = split_string(string)

    for line_index, line in enumerate(lines):
        for sentence_index, sentence in enumerate(line):
            for word_index, word in enumerate(sentence):
                sentence[word_index] = word.lower()

    string = join_string(lines)
    return string

def cap_all(string):

    lines = split_string(string)

    for line_index, line in enumerate(lines):
        for sentence_index, sentence in enumerate(line):
            for word_index, word in enumerate(sentence):
                sentence[word_index] = word.capitalize()

    string = join_string(lines)
    return string

def cap_first(string):

    lines = split_string(string)

    for line_index, line in enumerate(lines):
        for sentence_index, sentence in enumerate(line):
            for word_index, word in enumerate(sentence):
                if word_index == 0:
                    sentence[word_index] = word.capitalize()

    string = join_string(lines)
    return string

def snake_case(string):

    lines = split_string(string)
    
    for line_index, line in enumerate(lines):
        for sentence_index, sentence in enumerate(line):
            for word_index, word in enumerate(sentence):
                sentence[word_index] = word.lower()

    string = join_string(lines, s='_')
    return string

def undo_snake_case(string):

    lines = split_string(string, s='_')
    
    for line_index, line in enumerate(lines):
        for sentence_index, sentence in enumerate(line):
            for word_index, word in enumerate(sentence):
                sentence[word_index] = word.capitalize()

    string = join_string(lines, s=' ')
    return string  

def camel_case(string):

    lines = split_string(string, s=' ')
    
    for line_index, line in enumerate(lines):
        for sentence_index, sentence in enumerate(line):
            for word_index, word in enumerate(sentence):
                sentence[word_index] = word.capitalize()

    string = join_string(lines, s='')
    return string   
    

def modify(modification, paste=True):
    modifications = {
        'upper': make_upper,
        'lower': make_lower,
        'cap_all': cap_all,
        'snake_case': snake_case,
        'undo_snake_case': undo_snake_case,
        'camel_case': camel_case
        }
    copy_text()
    time.sleep(0.1)
    print('copied text')
    data = get_clipboard_data()
    modified_data = modifications[modification](data)
    copy_to_clipboard(modified_data)
    print('copied to clipboard')
    if paste == True:
        paste_text()
    print('Done')
    return {'data': data, 'modified_data': modified_data}

def undo():
    keyboard.press(Key.ctrl_l)
    keyboard.press('z')
    keyboard.release(Key.ctrl_l)