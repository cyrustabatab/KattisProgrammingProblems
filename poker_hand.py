from collections import defaultdict



def poker_hand():



    cards = input().split()
    

    rank_counts = defaultdict(int)
    

    maximum_rank_count = 0
    for rank,suit in cards:

        rank_counts[rank] += 1


        if rank_counts[rank] > maximum_rank_count:
            maximum_rank_count = rank_counts[rank]
    


    print(maximum_rank_count)

            


poker_hand()

















