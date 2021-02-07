import requests
import json

my_board = {}

def initialize():
    start_games = requests.get('http://rota.praetorian.com/rota/service/play.php?request=new&email=kalmpurcell@gmail.com')
    result = json.loads(start_games.text)
    cookies = start_games.cookies
    board = status(cookies)
    first_move = 'no'

    #************************************
    ''' FIRST MOVE '''
    if board.count('c') != 0 and space_empty(board,5):
        place(cookies,board,1)
    else:
        first_move = 'yes'
        place(cookies,board)
    #************************************
    ''' SECOND MOVE'''
    assign_my_board(board)

    #************************************
    '''THIRD MOVE'''
    #************************************

def space_empty(board,space):
    return board[int(space)] == '-'

def assign_my_board(board):
    my_board[1] = board[0]
    my_board[2] = board[1]
    my_board[3] = board[2]
    my_board[4] = board[3]
    my_board[5] = board[4]
    my_board[6] = board[5]
    my_board[7] = board[6]
    my_board[8] = board[7]
    my_board[9] = board[8]
    print(my_board,'assigned board')




def place(cookies,board,position=1, count=0):
    # my_board[str(board.find('c'))] == 'c'
    # count = int(count)
    # position = int(position)
    # while count < 3:
    requests.get(f'http://rota.praetorian.com/rota/service/play.php?request=place&location={position}' ,cookies = cookies)
        # count += 1
    # if space_empty(board,1):
    # place(cookies,position,count)


def move(old,new, cookies):
    requests.get(f'http://rota.praetorian.com/rota/service/play.php?request=move&from={old}&to={new}' ,cookies = cookies)

def status(cookies):
    status = requests.get('http://rota.praetorian.com/rota/service/play.php?request=status' ,cookies = cookies)
    print('STATUS',json.loads(status.text))
    return (json.loads(status.text)['data']['board'])

def reset(cookies):
    res =  requests.get('http://rota.praetorian.com/rota/service/play.php?request=new', cookies = cookies)


initialize()
#! if computer_wins = 1 then initialize again
#! if player_wins has changed then reset()



