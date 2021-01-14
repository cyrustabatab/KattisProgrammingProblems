

def kemija():

    
    vowels = {'a','e','i','o','u'}
    sentence = input()

    
    result = []
    i = 0
    while i < len(sentence):
        character = sentence[i]
        result.append(character)
        if character in vowels:
            i += 3
        else:
            i += 1
    


    print(''.join(result))




kemija()



