from collections import defaultdict



def dice():


    n,m = map(int,input().split())

    
    sums = defaultdict(int)
    
    maximum = float('-inf')
    for i in range(1,n + 1):
        for j in range(1,m + 1):
            s = i + j

            sums[s] += 1
            
            maximum = max(maximum,sums[s])



     
    for _sum,amount in sums.items():
        if amount == maximum:
            print(_sum)





dice()





