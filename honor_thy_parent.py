




def apaxian():


    string_1,string_2 = input().split()



    if string_1[-1] == 'e':
        name = string_1 + 'x' + string_2
    elif string_1[-1] in ('a','i','o','u'):
        name = string_1[:-1] + 'ex' + string_2
    elif string_1.endswith('ex'):
        name = string_1 + string_2
    else:
        name = string_1 + 'ex' + string_2



    print(name)



apaxian()




