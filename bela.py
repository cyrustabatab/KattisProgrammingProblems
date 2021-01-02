

def bela():


    hands,dominant_suit = input().split()

    hands = int(hands)
    
    dominant = {'A': 11,'K': 4,'Q': 3,'J': 20,'T': 10,'9': 14,'8': 0,'7': 0}
    not_dominant = {'A': 11,'K': 4,'Q': 3,'J': 2,'T': 10,'9': 0,'8': 0,'7': 0}


    score = 0
    for _ in range(hands *4):


        number,suit = input()


        if suit == dominant_suit:
            score += dominant[number]
        else:
            score += not_dominant[number]


    

    print(score)





bela()





