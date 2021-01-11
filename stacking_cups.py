




def cups():

    n = int(input())

    

    all_cups = []
    for _ in range(n):

        word_1,word_2 = input().split()


        if word_1.isdigit():
            value = (int(word_1)//2,word_2)
        else:
            value = (int(word_2),word_1)


        all_cups.append(value)
    



    all_cups.sort()


    for _,color in all_cups:
        print(color)


cups()












        


