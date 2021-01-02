




def abbreviate():


    all_names = input()

    result = [all_names[0]]
    
    previous_character = all_names[0]
    for i in range(1,len(all_names)):
        character = all_names[i]

        if previous_character == '-':
            result.append(character)


        previous_character = character


    
    print(''.join(result))




abbreviate()
