





def food():


    n = int(input())

    intervals = []
    for _ in range(n):
        start,end = map(int,input().split())
        intervals.append((start,end))
    


    intervals.sort()


    

    i = 0
    
    merged_intervals = []
    while i < len(intervals):

        start,end = intervals[i]

        j = i + 1

        while j < len(intervals) and intervals[j][0] <= end:
            end = max(intervals[j][1],end)
            j += 1

        
        merged_intervals.append((start,end))
        
        i = j

    days = 0
    for start,end in merged_intervals:
        days += (end - start + 1)
    
    print(days)

food()






























