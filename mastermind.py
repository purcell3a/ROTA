import requests, json, sys


if sys.version_info < (3,0):
  sys.exit('Python version < 3.0 does not support modern TLS versions. You will have trouble connecting to our API using Python 2.X.')

def start_game():
  r = requests.post('https://mastermind.praetorian.com/api-auth-token/', data={'email':'kalmpurcelld@gmail.com'})
  r.json()
  headers = r.json()
  headers['Content-Type'] = 'application/json'
  next_level(1,headers)

# Interacting with the game
def next_level(level,headers):

  print('level',level)
  r = requests.get(f'https://mastermind.praetorian.com/level/{level}/', headers=headers)
  r = r.json()
  print(r)

  # ************************************************ VARIABLES
  final_guess = []
  correct_numbers = []
  numbers = [0,1,2,3,4,5]
  # ************************************************

  # ?  ************************************************ START
  find_numbers(level,headers,final_guess,correct_numbers,numbers)


def find_numbers(level,headers,final_guess,correct_numbers,numbers,idx=0,count=0):
    ''' This is a recursive function that finds all the correct numbers '''

    # ************************************************ VARIABLES
    noise=[7,8,9,10]
    # ************************************************

    for num in numbers:
        count = count + 1
        if count < 5:

            noise[idx] = num
            response = guess(noise, headers)

            if response == [1,1]:
                final_guess.append(num)
                idx += 1
            if response == [1,0]:
                correct_numbers.append(num)
            numbers.remove(num)
            find_numbers(level,headers,final_guess,correct_numbers,numbers,idx,count)
            break

        if count < 6:
            check_nums(level,headers,final_guess,correct_numbers,numbers,idx)


def check_nums(level,headers,final_guess,correct_numbers,numbers,idx):
    ''' This function sorts where to go next based on how many we know for sure '''

    if idx == 0:
        find_first(level,headers,final_guess,correct_numbers,numbers,idx)

    if idx == 1:
        find_second(level,headers,final_guess,correct_numbers,numbers,idx)

    if idx == 2:
        if len(correct_numbers) == 1:
            find_second(level,headers,final_guess,correct_numbers,numbers,idx)
        else:
            sort_nums(level,headers,final_guess,correct_numbers,numbers,idx)

    if idx == 3:
        last_guess(level,headers,final_guess,correct_numbers,numbers,idx)


def find_first(level,headers,final_guess,correct_numbers,numbers,idx):
  ''' this function finds first and narrows down possibilities for second '''

    # ************************************************
    not_second = []
    correct_count = len(correct_numbers)
    noise=[7,8,9,10]
    # ************************************************
    noise[0] = numbers[0]
    noise[1] = correct_numbers[0]
    response = guess(noise, headers)

    if response == [1,1]:
        final_guess = [numbers[1],correct_numbers[0]]
        correct_numbers = correct_numbers[1:]
        sort_nums(level,headers,final_guess,correct_numbers,numbers,idx)

    if response == [2,2]:
        final_guess = [numbers[0],correct_numbers[0]]
        correct_numbers = correct_numbers[1:]
        sort_nums(level,headers,final_guess,correct_numbers,numbers,idx)

    if response == [2,0]:
        final_guess = [numbers[1]]
        correct_numbers.append(numbers[0])
        idx += 1
        find_second(level,headers,final_guess,correct_numbers,numbers,idx)

    if response == [2,1]:
        final_guess = [numbers[0]]
        not_second = correct_numbers[0]
        correct_numbers = correct_numbers[1:]
        if correct_count == 2:
            correct_numbers.append(numbers[1])
        correct_numbers.append(not_second)
        idx +=1
        find_second(level,headers,final_guess,correct_numbers,numbers,idx)

def find_second(level,headers,final_guess,correct_numbers,numbers,idx):

    # ************************************************ VARIABLES
    correct_count = len(correct_numbers)
    noise=[7,8,9,10]
    print('final',final_guess,'correct',correct_numbers,'numbers',numbers)
    # ************************************************

    if correct_count == 3:

        for num in correct_numbers[:2]:
            if num < final_guess[0]:
                noise[idx] = num
                print('line 132', noise)
                response = guess(noise, headers)
                if response == [1,1]:
                    final_guess.append(num)
                    correct_numbers.remove(num)
                    sort_nums(level,headers,final_guess,correct_numbers,numbers,idx)
        final_guess.append(correct_numbers[-1])
        correct_numbers.remove(correct_numbers[-1])
        sort_nums(level,headers,final_guess,correct_numbers,numbers,idx)

    if correct_count == 2:
        if len(final_guess) == 2:
            sort_nums(level,headers,final_guess,correct_numbers,numbers,idx)
        else:
            noise[idx] = numbers[0]
            response = guess(noise, headers)
            if response == [1,0]:
                correct_numbers.append(noise[idx])
                find_second(level,headers,final_guess,correct_numbers,numbers,idx)
            if response == [0,0]:
                correct_numbers.append(numbers[1])
                numbers = []
                find_second(level,headers,final_guess,correct_numbers,numbers,idx)
            if response == [1,1]:
                final_guess.append(numbers[0])
                sort_nums(level,headers,final_guess,correct_numbers,numbers,idx)

    if correct_count == 1:
        for num in numbers:
            noise[idx] = num
            print('line 158', noise)
            response = guess(noise, headers)
            if response == [1,1]:
                final_guess.append(noise[idx])
                sort_nums(level,headers,final_guess,correct_numbers,numbers,idx)
            else:
                correct_numbers.append(num)
                sort_nums(level,headers,final_guess,correct_numbers,numbers,idx)


def sort_nums(level,headers,final_guess,correct_numbers,numbers,idx):

    # ************************************************ VARIABLES
    if len(correct_numbers) == 0:
        correct_numbers = numbers
    noise=[7,8,9,10]
    print('final',final_guess,'correct',correct_numbers,numbers)
    # ************************************************

    # ? ***********************************************  OG GUESS
    noise[:2] = final_guess
    noise[2:] = correct_numbers
    response = guess(noise, headers)
    # ? ***********************************************


    if response != {'message': 'Onto the next level'}:
      noise[2] = correct_numbers[1]
      noise[3] = correct_numbers[0]
      response = guess(noise,headers)

    # TODO *********************************************** not letting me move to next level
    if response == {'message': 'Onto the next level'}:
        level += 1
        next_level(level,headers)
    # TODO ***********************************************


def last_guess(level,headers,final_guess,correct_numbers,numbers,idx):

    # ************************************************
    print('final',final_guess,'correct',correct_numbers,'numbers',numbers)
    correct_count = len(correct_numbers)
    noise=[7,8,9,10]
    # ************************************************

    if correct_count == 0:
        for num in numbers:
            noise = [final_guess,num]
            response = guess(noise,headers)

    if correct_count == 1:
            noise = [final_guess,correct_numbers]
            response = guess(noise,headers)

    if response == {'message': 'Onto the next level'}:
        level += 1
        next_level(level,headers)



def guess(guess,headers):
  r = requests.post('https://mastermind.praetorian.com/level/1/', data=json.dumps({'guess':guess}), headers=headers)
  re = r.json()

  if re == {'message': 'Onto the next level'}:
      return re
  else:
    return re.get('response')


start_game()