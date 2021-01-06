



def no_duplicates():


    line = input()

    words = line.split()


    seen = set()


    for word in words:
        if word in seen:
            print('no')
            break

        seen.add(word)
    else:
        print('yes')



no_duplicates()


