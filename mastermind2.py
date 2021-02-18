import requests, json, sys


if sys.version_info < (3,0):
  sys.exit('Python version < 3.0 does not support modern TLS versions. You will have trouble connecting to our API using Python 2.X.')

def start_game():
  r = requests.post('https://mastermind.praetorian.com/api-auth-token/', data={'email':'olaljhghr@sslkade.com'})
  r.json()
  headers = r.json()
  headers['Content-Type'] = 'application/json'
  next_level(1,headers)

# Interacting with the game
def next_level(level,headers):
  r = requests.get(f'https://mastermind.praetorian.com/level/{level}/', headers=headers)
  r.json()

  first_guess = [8,9,10]
  final_guess = []
  correct_numbers = []
  numbers = [0,1,2,3,4,5]

  # ************************************************
  for num in numbers[0:4]:
      response = guess([num] + [8,9,10],headers)
      if response == [1, 1]:
        final_guess.append(num)
        found_first(final_guess,correct_numbers,numbers,headers)
        break
      if response == [1,0]:
        correct_numbers.append(num)
      numbers.remove(num)
  sort_numbers(final_guess,correct_numbers,numbers,headers)
  # ************************************************

def found_first(final_guess,correct_numbers,numbers,headers):
  print('FOUND FIRST')
  for num in numbers[0:-1]:
    response = guess([10] + [num] + [8,9],headers)
    print('line 41',response)
    if response == [1, 1]:
      final_guess.append(num)
      found_second(final_guess,correct_numbers,numbers,headers)
      exit()
    if response == [1,0]:
      correct_numbers.append(num)
    numbers.remove(num)
  print('DID NOT FIND SECOND')
  sort_numbers(final_guess,correct_numbers,numbers,headers)

def found_second(final_guess, correct_numbers,numbers,headers):
  print('FOUND SECOND')
  for num in numbers[0:-1]:
    response = guess([8,10] + [num] + [9],headers)
    if response == [1, 1]:
      final_guess.append(num)
      sort_numbers(final_guess,correct_numbers,numbers,headers)
      exit()
    if response == [1,0]:
      correct_numbers.append(num)
    numbers.remove(num)
  if len(correct_numbers + final_guess) == 4:
    numbers = []
  sort_numbers(final_guess,correct_numbers,numbers,headers)
  exit()


def sort_numbers(final_guess,correct_numbers, numbers,headers):
  print('correct',correct_numbers,'numbers',numbers,'final_guess', final_guess)
  if final_guess != []:
    if len(correct_numbers + final_guess) == 4:
      right_numbers(final_guess,correct_numbers,headers)
      exit()
    else:
      response = guess(final_guess + numbers + correct_numbers,headers)
      print('line 86',final_guess + numbers + correct_numbers)
  else:
    find_first(final_guess,correct_numbers, numbers,headers)


def find_first(final_guess,correct_numbers, numbers,headers):
  if len(correct_numbers) > 2:
    response = guess(numbers[0:-1] + [7,8,9],headers)
    if response == [1,1]:
      final_guess.append(numbers[0:-1])
      numbers = [numbers[-1]]
      print(numbers)
    if response == [0,0]:
      final_guess == [numbers[-1]]
      numbers = []
      sort_last_three(final_guess, correct_numbers,numbers)
  else:
    response = guess(numbers + [8,9],headers)
    if response == [2,2]:
      final_guess = numbers
      sort_numbers(final_guess, correct_numbers,numbers,headers)
    if response == [2,1]:
      numbers_backwards = numbers[-1:0]
      print('response was 2,1', numbers_backwards)
      response = guess(numbers_backwards + [8,9],headers)
    if response == [1,1]:
      final_guess.append([numbers[0]])
      print('found first in sort', final_guess,correct_numbers)
    if response == [2,0]:
      final_guess.append([numbers[-1]])
      correct_numbers.append([numbers[0]])
      sort_last_three(final_guess,correct_numbers,headers)

def sort_last_three(final_guess, correct_numbers,headers):
  print('correct',correct_numbers,'final_guess', final_guess)
  print('sorting last three')
  response = guess(final_guess + [8,9] + [correct_numbers[-1]],headers)
  if response == [2,2]:
    response = guess(final_guess + correct_numbers,headers)
  if response == [2,1]:
    response == guess(final_guess + correct_numbers)


def guess(guess,headers):
  r = requests.post('https://mastermind.praetorian.com/level/1/', data=json.dumps({'guess':guess}), headers=headers)
  re = r.json()
  print(re.get('response'))
  return re.get('response')


def right_numbers(final_guess, correct_numbers,headers):
  response = guess(final_guess + correct_numbers,headers)
  if response != [4,4]:
    response == guess(final_guess + correct_numbers[-1:0],headers)
    print('line 130',final_guess + correct_numbers[-1:0])
  else:
    print('response on line 132',response)
    print('next level')


start_game()