from collections import defaultdict



def cetvrta():


    n= 3

    
    x_counts = defaultdict(int)
    y_counts = defaultdict(int)
    for _ in range(n):
        x,y = map(int,input().split())

        x_counts[x] += 1
        y_counts[y] += 1



    
    
    for x,x_count in x_counts.items():
        if x_count != 2:
            missing_x = x
    


    for y,y_count in y_counts.items():
        if y_count != 2:
            missing_y = y

    

    print(missing_x,missing_y)

        
    

cetvrta()







