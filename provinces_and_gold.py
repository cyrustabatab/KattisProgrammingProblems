from collections import OrderedDict




def provinces_and_gold():



    gold,silver,copper = map(int,input().split())
    

    buying_power= 3 * gold + 2 * silver + copper
    

    victory = ((8, 'province'),(5, 'duchy'),(2, 'estate'))
    treasure = ((6, 'gold'),(3, 'silver'),(0, 'copper'))

    

    best_victory = None
    for value,item in victory:
        if value <= buying_power:
            best_victory = item
            break



    for value,item in treasure:

        if value <= buying_power:
            best_treasure = item
            break




    if best_victory:
        print(f"{best_victory.capitalize()} or {best_treasure.capitalize()}")
    else:
        print(best_treasure)



provinces_and_gold()










    
    























