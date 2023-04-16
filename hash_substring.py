# Makars Sinakovs 221RDB519
def read_input():
    letter = input().strip()
    if letter not in ('I', 'F'):
        raise ValueError('Invalid input')
    if letter == 'I':
        pattern = input().strip()
        text = input().strip()
        return pattern, text
    else:
        filename = input().strip()
        try:
            with open(f"./tests/{filename}", "r") as file:
                lines = file.readlines()
                pattern = lines[0].strip()
                text = lines[1].strip()
                return pattern, text
        except FileNotFoundError:
            raise ValueError('File not found')

def print_occurrences(output):
    if not output:
        print('Pattern not found')
    else:
        print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    pattern_len = len(pattern)
    text_len = len(text)
    prime = 256
    pattern_hash = 0
    text_hash = 0
    
    for i in range(pattern_len):
        pattern_hash += ord(pattern[i]) * pow(prime, i)
        text_hash += ord(text[i]) * pow(prime, i)
 
    res = []
    for i in range(text_len - pattern_len + 1):
        if text_hash == pattern_hash:
            match = True
            for j in range(pattern_len):
                if text[i+j] != pattern[j]:
                    match = False
                    break
            if match:
                res.append(i)
        if i < text_len - pattern_len:
            text_hash = (text_hash - ord(text[i]) * pow(prime, 0)) // prime + ord(text[i+pattern_len]) * pow(prime, pattern_len-1)
    return res

if __name__ == '__main__':
    try:
        pattern, text = read_input()
        occurrences = get_occurrences(pattern, text)
        print_occurrences(occurrences)
    except Exception as e:
        print(e)