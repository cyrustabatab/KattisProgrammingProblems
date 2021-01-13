




def drm_message():


    message = input()

    message_length = len(message)
    
    half_message_length = message_length//2

    first_half = message[:half_message_length]
    second_half = message[half_message_length:]


    
    
    
    result = []
    for string in (first_half,second_half):
        new_string = []
        rotation_value = 0
        for character in string:
            value = ord(character) - ord('A')
            rotation_value += value

        for character in string:

            new_ord = (ord(character) - ord('A') + rotation_value) % 26
            new_string.append(chr(new_ord + ord('A')))


        result.append(''.join(new_string))



    string_1,string_2 = result

    final_string = []
    for c1,c2 in zip(string_1,string_2):
        new_ord = (ord(c1) - ord("A") + (ord(c2) - ord('A')))% 26

        final_string.append(chr(new_ord + ord('A')))




    print(''.join(final_string))








drm_message()















