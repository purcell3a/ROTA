


def sort_nums(headers,final_guess,correct_numbers,idx):
    print('final',final_guess,'correct',correct_numbers)

    # ************************************************
    noise=[7,8,9,10]
    # ************************************************

    noise[:2] = final_guess
    noise[2:] = correct_numbers
    print('line 79', noise)
    response = guess(noise, headers)
    if response == [4,4]:
      print('NEXT LEVEL')
    if response == [4,2]:
      noise[2] = correct_numbers[1]
      noise[3] = correct_numbers[0]
      response = guess(noise,headers)
      print('NEXT LEVEL LINE 87')


