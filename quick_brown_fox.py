from string import ascii_lowercase



def fox():


    n = int(input())

    alphabet = {c for c in ascii_lowercase}
    for _ in range(n):
        
        letters = alphabet.copy()
        phrase = input()

        for character in phrase:
            character = character.lower()
            if character.isalpha():
                if character in letters:
                    letters.remove(character)

        

        
        if letters:
            sorted_letters =sorted(letters)
             
            print("missing",end=' ')
            for letter in sorted_letters:
                print(letter,end='')
            print()
        else:
            print('pangram')

        


fox()

