import requests
import time

if __name__ == '__main__':
    url = 'https://api.stackexchange.com/2.3/questions'
    date = int(time.time())
    params = {
        'fromdate' : str(date - 172800),
        'todate' : str(date),
        'order' : 'desc',
        'sort' : 'creation',
        'tagged' : 'Python',
        'site' : 'stackoverflow'
    }
    response = requests.get(url, params=params, timeout=5)
    print('\nСписок тем вопросов созданных за последние двое суток по теме - Python:\n')
    for i in response.json()['items']:
        print(i['title'])