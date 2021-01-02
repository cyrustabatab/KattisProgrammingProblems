




def homework():

    
    s = input()

    

    parts = s.split(';')
    problems = 0
    for part in parts:

        if '-' in part:
            hyphen_index = part.index('-')
            number_1,number_2 = int(part[:hyphen_index]),int(part[hyphen_index +1:])
            problems += (number_2 - number_1 + 1)
        else:
            problems += 1


    print(problems)



homework()


