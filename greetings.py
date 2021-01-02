



def greetings():


    s = input()


    number_of_e = len(s) - 2

    
    result_e = number_of_e * 2
    result = ['h','e' * result_e,'y']

    print(''.join(result))



greetings()


