





def hissing():


    s = input()


    for i in range(len(s) - 1):
        character =s[i]
        if character == 's':
            if s[i +1] == 's':
                print('hiss')
                break
    else:
        print('no hiss')



    

hissing()
