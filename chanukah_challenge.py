




def chanukah():


    n = int(input())


    for i in range(n):

        _,days = map(int,input().split())


        total = (days * (days + 1))//2 + days

        print(f"{i +1} {total}")





chanukah()








