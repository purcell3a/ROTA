import requests, json, sys


if sys.version_info < (3,0):
  sys.exit('Python version < 3.0 does not support modern TLS versions. You will have trouble connecting to our API using Python 2.X.')

def start_game():
  r = requests.post('https://mastermind.praetorian.com/api-auth-token/', data={'email':'orwasdfefgd@sslkade.com'})
  r.json()
  headers = r.json()
  headers['Content-Type'] = 'application/json'
  next_level(1,headers)

# Interacting with the game
def next_level(level,headers):
  r = requests.get(f'https://mastermind.praetorian.com/level/{level}/', headers=headers)
  r.json()

  final_guess = []
  correct_numbers = []
  numbers = [0,1,2,3,4,5]
  find_numbers(headers,final_guess,correct_numbers,numbers)
  # ************************************************

def find_numbers(headers,final_guess,correct_numbers,numbers,idx=0,count=0):
    print('first count', count)
    # ************************************************
    noise=[7,8,9,10]
    # ************************************************
    
    for num in numbers:
        if count < 4:
            count = count + 1
            print('count',count)

            noise[idx] = num
            response = guess(noise, headers)

            if response == [1,1]:
                final_guess.append(num)
                idx += 1
            if response == [1,0]:
                correct_numbers.append(num)
            numbers.remove(num)
            find_numbers(headers,final_guess,correct_numbers,numbers,idx,count)
            break
        else:
            sort_numbers(final_guess,correct_numbers,numbers,noise)


def sort_numbers(final_guess,correct_numbers,numbers,noise):
    print('next function')


def guess(guess,headers):
  r = requests.post('https://mastermind.praetorian.com/level/1/', data=json.dumps({'guess':guess}), headers=headers)
  re = r.json()
  print(re.get('response'))
  return re.get('response')


start_game()