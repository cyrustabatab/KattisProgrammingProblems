



def judging_moose():



    left,right = map(int,input().split())
    

    if left == right == 0:
        print("Not a moose")
    elif left == right:
        print(f"Even {2 * left}")
    else:
        maximum = max(left,right) * 2
        print(f"Odd {maximum}")


    

judging_moose()
















