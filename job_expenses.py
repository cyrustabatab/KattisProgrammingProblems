




def job_expenses():
    

    n = int(input())

    expenses = 0

    numbers =map(int,input().split())


    for number in numbers:
        if number < 0:
            expenses += abs(number)
    

    print(expenses)




job_expenses()







