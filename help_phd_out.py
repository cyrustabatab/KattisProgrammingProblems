



def help_phd_out():


    n= int(input())


    for _ in range(n):
        problem = input()

        if problem[0]== 'P':
            print('skipped')
        else:
            print(eval(problem))




help_phd_out()



