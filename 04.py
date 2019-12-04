possible_passwords = [str(i) for i in range(108457,562041+1)]

def detect_adjacent_1(string):
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
        
def detect_adjacent_2(string):
    for i in range(len(string)):
        group = string[i:i+3]
        group = [i for i in group]
        if len(group) == 3:
            same = all(x == group[0] for x in group)
            
        if same
            
        
matches = [i for i in possible_passwords if detect_adjacent(i) and detect_increasing(i)]
