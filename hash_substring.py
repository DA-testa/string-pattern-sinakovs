# Makars Sinakovs 221RDB519
def read_input():
    letter=input()
    if letter =="I":
        pattern=input()
        text=input()
        return(pattern.rstrip(),text.rstrip())
    if letter =="F":
        filename=input()
        with open(("./tests/"+filename),"r") as file:
            pattern=file.readline()
            text=file.readline()
        return(pattern.rstrip(),text.rstrip())

def print_occurrences(output): 
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    pattern_len=len(pattern)
    text_len =len(text)
    prime = 256
    pattern_hash=0
    text_hash=0
    
    for i in range(pattern_len):
        pattern_hash=pattern_hash+ord(pattern[i])*pow(prime,i)
        text_hash=text_hash+ord(text[i])*pow(prime,i)
 
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
            text_hash = (text_hash - ord(text[i]) * pow(prime, 0)) / prime + ord(text[i+pattern_len]) * pow(prime, pattern_len-1)
    return res

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))