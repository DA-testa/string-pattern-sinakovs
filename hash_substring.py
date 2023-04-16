def main():
    letter=input()
    if letter =="I":
        line=input()
        data=line.split(" ")
        position=rabinKarpAlgorithm(data[0],data[1])
        print(position)

    if letter =="F":
        filename=input()
        with open(("./test/"+filename,"r")) as file:
            line=file.read()
            data=line.split(" ")
            position=rabinKarpAlgorithm(data[0],data[1])
            print(position)

def rabinKarpAlgorithm(pattern, text):
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

if __name__ == "__main__":
    main()