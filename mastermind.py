import requests, json, sys


if sys.version_info < (3,0):
  sys.exit('Python version < 3.0 does not support modern TLS versions. You will have trouble connecting to our API using Python 2.X.')

def start_game():
  r = requests.post('https://mastermind.praetorian.com/api-auth-token/', data={'email':'other@lipade.com'})
  r.json()
  headers = r.json()
  headers['Content-Type'] = 'application/json'
  next_level(headers)

# Interacting with the game
def next_level(headers):
  r = requests.get('https://mastermind.praetorian.com/level/1/', headers=headers)
  r.json()

  final_guess = []
  correct_numbers = []
  numbers = [0,1,2,3,4,5,6]

  # ************************************************
  for num in numbers[0:3]:
      response = guess([num] + [8,9,10],headers)
      if response == [1,1]:
        final_guess.append(num)
        numbers.remove(num)
        found_first(final_guess,correct_numbers,numbers,headers)
        break
      if response == [1,0]:
          correct_numbers.append(num)
          numbers.remove(num)
      if response == [0,0]:
          numbers.remove(num)
  no_first(final_guess,correct_numbers,numbers,headers)
  # ************************************************



def found_first(final_guess,correct_numbers,numbers,headers):
  print('FOUND FIRST')
  while len(correct_numbers) < 3:
    for index,num in enumerate(numbers):
      response = guess(final_guess + [num] + [8,9],headers)
      if response == [2,2]:
        final_guess.append(num)
        numbers.remove(num)
        print('FIRST',final_guess,'correct',correct_numbers,'nums',numbers)
        found_second(final_guess,correct_numbers,numbers,headers)
        break
      if response == [2,1]:
          correct_numbers.append(num)
          numbers.remove(num)
      if response == [1,1]:
          correct_numbers.append(num)
          numbers.remove(num)
          # WE NEED A FUNCTION FOR WHEN WE DON'T FIND THE SECOND


def no_first(final_guess,correct_numbers,numbers,headers):
  print('DIDNT FIND FIRST')
  if len(correct_numbers) == 1:
    now_sort(final_guess,correct_numbers,numbers,headers)
  else:


def now_sort(final_guess,correct_numbers,numbers,headers):
  for num in numbers:
    response = guess([num]+[8,9] + correct_numbers,headers)
    if response == [2,2]:
      final_guess.append(num)
      final_guess.append(correct_numbers)
    elif response == [2,1]:
      response = guess([num]+ correct_numbers +[8,9],headers)

    elif response == [2,0]

def found_second(final_guess,correct_numbers,numbers,headers):
  print('FOUND SECOND')
  while len(correct_numbers) < 2:
    for num in numbers:
      response = guess(final_guess + [num] + [8],headers)
      if response == [3,3]:
          final_guess.append(num)
          numbers.remove(num)
          print('THIRD',final_guess,'correct',correct_numbers,'nums',numbers)
          found_third(final_guess,correct_numbers,numbers,headers)
          break
      if response == [3,2]:
          correct_numbers.append(num)
          numbers.remove(num)
      if response[2,2]:
          numbers.remove(num)
  print('SECOND',final_guess,'correct',correct_numbers,'nums',numbers)
  third_step(final_guess,correct_numbers,numbers)

def found_third(final_guess,correct_numbers,numbers,headers):
  print('FOUND THIRD')
  if correct_numbers != []:
    response = guess(final_guess + correct_numbers,headers)
    print('DID WE DO IT?!', response)
  else:
    for num in numbers:
      response = guess(final_guess + [num],headers)
      if response == [4,4]:
          final_guess.append(num)
          numbers.remove(num)
          print('did we do it????',final_guess,'correct',correct_numbers,'nums',numbers)
          # START A NEW LEVEL HERE
          break
      if response == [3,3]:
          numbers.remove(num)

def third_step(final_guess,correct_numbers,numbers):
  print('final',final_guess,'correct',correct_numbers,'nums',numbers)


def guess(guess,headers):
  r = requests.post('https://mastermind.praetorian.com/level/1/', data=json.dumps({'guess':guess}), headers=headers)
  re = r.json()
  print(re)
  return re.get('response')



def right_numbers(guess,headers):
  r = requests.post('https://mastermind.praetorian.com/level/1/', data=json.dumps({'guess':guess}), headers=headers)
  re = r.json()
  print('made it to the right numbers')


# def restart():
#   r = requests.post(f'https://mastermind.praetorian.com/reset/')
#   print(r.keys())
# restart()

start_game()



# import requests, json, sys
# if sys.version_info < (3,0):
#   sys.exit('Python version < 3.0 does not support modern TLS versions. You will have trouble connecting to our API using Python 2.X.')
# email = 'other@lipade.com' # Change this!
# r = requests.post('https://mastermind.praetorian.com/api-auth-token/', data={'email':email})
# r.json()
# # > {'Auth-Token': 'AUTH_TOKEN'}
# headers = r.json()
# headers['Content-Type'] = 'application/json'

# # Interacting with the game
# r = requests.get('https://mastermind.praetorian.com/level/1/', headers=headers)
# r.json()
# # > {'numGladiators': 4, 'numGuesses': 8, 'numRounds': 1, 'numWeapons': 6}
# r = requests.post('https://mastermind.praetorian.com/level/1/', data=json.dumps({'guess':[1,2,3,4]}), headers=headers)
# re = r.json()
# print (re)
# # > {'response': [2, 1]}