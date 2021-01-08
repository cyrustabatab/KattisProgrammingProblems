



def differences():


    n = int(input())


    for _ in range(n):

        word_1,word_2 = input(),input()
        
        print(word_1)
        print(word_2)

        for character_1,character_2 in zip(word_1,word_2):
            if character_1 != character_2:
                print('*',end='')
            else:
                print('.',end='')

        print()
        print()






differences()





