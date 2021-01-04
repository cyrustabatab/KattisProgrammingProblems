from collections import defaultdict




def seven_wonders():


    cards = input()

    

    card_counts = {'T': 0,'C': 0,'G': 0}
    
    for card in cards:

        card_counts[card] += 1

    

    points = 0
    min_count = float("inf")
    for card,count in card_counts.items():

        points += count**2

        if count < min_count:
            min_count = count



    points += 7 * min_count


    print(points)


seven_wonders()































        






