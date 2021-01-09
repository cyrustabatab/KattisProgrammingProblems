






def correct_number():


    numbers = map(int,input().split())
    

    correct_amounts = [1,1,2,2,2,8]
    

    for i,number in enumerate(numbers):
        
        correct_amount = correct_amounts[i]
        amount = correct_amount - number

        print(amount,end=' ')


    print()



correct_number()







