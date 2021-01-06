


def parking():


    n = int(input())


    for _ in range(n):

        num_stores = input()

        stores = map(int,input().split())


        minimum_value = float("inf")
        maximum_value = float("-inf")

        for store in stores:
            maximum_value = max(store,maximum_value)
            minimum_value = min(store,minimum_value)




        
        distance_walked = (maximum_value - minimum_value) * 2
        print(distance_walked)

        




parking()











