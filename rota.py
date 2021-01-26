import requests
import json


def initialize():
    start_games = requests.get('http://rota.praetorian.com/rota/service/play.php?request=new&email=kalmpurcell@gmail.com')
    result = json.loads(start_games.text)
    cookies = start_games.cookies
    status(cookies)

def place(position):
    requests.get(f'http://rota.praetorian.com/rota/service/play.php?request=place&location={position}' ,cookies = cookies)

def move(old,new):
    requests.get(f'http://rota.praetorian.com/rota/service/play.php?request=move&from={old}&to={new}' ,cookies = cookies)

def status(cookies):
    status = requests.get('http://rota.praetorian.com/rota/service/play.php?request=status' ,cookies = cookies)
    print (json.loads(status.text))

def reset():
    res =  requests.get('http://rota.praetorian.com/rota/service/play.php?request=new')

initialize()
