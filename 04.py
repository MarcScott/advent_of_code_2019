import re

possible_passwords = [str(i) for i in range(108457,562041+1)]

def detect_adjacent(string):
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            return True
    return False

def detect_increasing(string):
    increasing = True
    for i in range(len(string)-1):
        if int(string[i]) > int(string[i+1]):
            increasing = False
    return increasing

def doubles(string):
    number = set(re.findall(r'([0-9])\1', string))
    repeats = [re.findall(r"({0}{0}+)".format(c), string) for num in numbers]
    if [x for x in repeats if len(x[0]) == 2]:
        return True
    else:
        return False        

matches_1 = [i for i in possible_passwords if detect_adjacent(i) and detect_increasing(i)]
matches_2 = [i for i in possible_passwords if doubles(i) and detect_increasing(i)]
