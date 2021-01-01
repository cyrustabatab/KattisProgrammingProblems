




def nasty_hacks():


    n = int(input())


    for _ in range(n):
        r,e,c = map(int,input().split())


        true_revenue = e - c

        if true_revenue > r:
            print("advertise")
        elif true_revenue < r:
            print("do not advertise")
        else:
            print("does not matter")






nasty_hacks()

