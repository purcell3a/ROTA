# Tried recursion


  my_list = [22,33,77,22,33]
 my_list = [99 if i==22 else i for i in my_list]
 print(my_list)
  find_numbers(headers,first_guess,final_guess,correct_numbers,numbers)
def find_numbers(headers,first_guess,final_guess,correct_numbers,numbers,ins=0,response1=2,response2=1,response3=0,slicer=0):

  while len(correct_numbers) < 2:
    for num in numbers:
      print('ANOTHER GUESS')
      first_guess.insert(ins,num)
      response = guess(first_guess, headers)
      first_guess.pop(0)
      print('response',response)
      if sum(response) == response1:
        final_guess.append(num)
        numbers.remove(num)
        ins += 1
        response1 += 2
        response2 += 1
        response3 += 2
        find_numbers(first_guess,final_guess,correct_numbers,numbers,ins,response1,response2,response3,slicer,headers)
        print('FOUND FIRST')
        break
      if sum(response) == response2:
        correct_numbers.append(num)
        numbers.remove(num)
      if sum(response) == response3:
        numbers.remove(num)
  print('never found first')
