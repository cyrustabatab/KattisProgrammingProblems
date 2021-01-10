





def puzzle():

    word = input()


    i = 0


    name = 'PER'
    name_index = 0

    count = 0
    while i < len(word):
        if word[i] != name[name_index]:
            count += 1


        name_index = (name_index + 1) % len(name)
        i += 1
    
    print(count)


puzzle()












