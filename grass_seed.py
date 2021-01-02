




def grass_seed():


    cost = float(input())

    number_of_lawns_to_sow = int(input())

    
    result = 0
    for _ in range(number_of_lawns_to_sow):
        width,length = map(float,input().split())
        result += cost * (width * length)


    print(f"{result:.6f}")




grass_seed()










