


def roaming_romans():


    
    n = 5280
    r = 4854
    miles = float(input())


    roman_miles = miles *  n / r

    
    roman_paces = roman_miles * 1000
    print(round(roman_paces))



roaming_romans()


