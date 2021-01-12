



def most_correct():



    adrian = ['A','B','C']
    bruno = ['B','A','B','C']
    goran = ['C','C','A','A','B','B']


    adrian_index = bruno_index = goran_index = 0
    

    adrian_correct = bruno_correct = goran_correct= 0
    

    n = input()

    answers = input()


    for answer in answers:
        adrian_answer,bruno_answer,goran_answer = adrian[adrian_index],bruno[bruno_index],goran[goran_index]

        if adrian_answer == answer:
            adrian_correct += 1

        if bruno_answer == answer:
            bruno_correct += 1

        if goran_answer == answer:
            goran_correct += 1


        adrian_index = (adrian_index + 1) % len(adrian)
        bruno_index = (bruno_index + 1) % len(bruno)
        goran_index = (goran_index + 1) % len(goran)



    maximum = max(adrian_correct,bruno_correct,goran_correct)
    
    print(maximum)
    if maximum == adrian_correct:
        print('Adrian')
    if maximum == bruno_correct:
        print('Bruno')

    if maximum == goran_correct:
        print('Goran')
    

most_correct()























