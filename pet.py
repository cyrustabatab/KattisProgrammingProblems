



def pet():

        

    n = 5
    

    max_score = 0
    winner = None
    for i in range(1,n + 1):

        grades= map(int,input().split())

        score = sum(grades)

        if score > max_score:
            max_score = score
            winner= i
    


    print(winner,max_score)




pet()






