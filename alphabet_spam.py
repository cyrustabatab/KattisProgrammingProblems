




def spam():

    word = input()

    
    whitespace_count = lowercase_count = uppercase_count = symbol_count = 0
    for character in word:
        if character == '_':
            whitespace_count += 1
        elif character.islower():
            lowercase_count += 1
        elif character.isupper():
            uppercase_count += 1
        else:
            symbol_count += 1

    
    length = len(word)


    print(whitespace_count/length)
    print(lowercase_count/length)
    print(uppercase_count/length)
    print(symbol_count/length)


spam()

