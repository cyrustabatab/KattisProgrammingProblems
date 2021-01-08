





def terrace():


    limit,number_of_events =map(int,input().split())
    

    current_amount = 0

    refused_amount = 0
    for _ in range(number_of_events):
        event,amount = input().split()
        
        amount = int(amount)
        if event == 'enter':
            if current_amount + amount > limit:
                refused_amount += 1
            else:
                current_amount += amount
        else:
            current_amount -= amount

    


    print(refused_amount)




terrace()




