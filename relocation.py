



def relocation():


    n,requests = map(int,input().split())

    
    company_locations = map(int,input().split())

    
    company_to_location = {}
    for i,company_location in enumerate(company_locations):
        company_to_location[i +1] = company_location


    for _ in range(requests):
        query,number_1,number_2 = map(int,input().split())

        if query == 1:
            company_to_location[number_1] = number_2
        else:
            distance = abs(company_to_location[number_1] - company_to_location[number_2])
            print(distance)
            


relocation()











