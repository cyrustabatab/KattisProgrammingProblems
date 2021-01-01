





def cities_visited():




    n = int(input())


    for _ in range(n):
        
        cities = set()
        
        work_trips = int(input())


        for _ in range(work_trips):

            city = input()

            if city not in cities:
                cities.add(city)

    
        
        print(len(cities))





cities_visited()


        

