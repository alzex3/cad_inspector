import requests as rq
from pprint import pprint
kad_numbers = []

with open('test_kad.txt') as f:
    for number in f:
        kad_numbers.append(number.strip())

resp = rq.get(url=f'http://rosreestr.ru/fir_lite_rest/api/gkn/fir_lite_object/52:18:0050135:385')
pprint(resp.json()['type'])
if resp.json()['type'] == 'flat':
    pprint(resp.json())
    pprint(resp.json()['objectCn'])
    pprint(resp.json()['objectData']['actualDate'])
    pprint(resp.json()['objectData']['address']['mergedAddress'])
    pprint(resp.json()['objectData']['address']['note'])
    pprint(resp.json()['objectData']['cadRecordDate'])
    pprint(resp.json()['objectData']['dateCreated'])
    pprint(resp.json()['objectData']['flat']['actualDate'])
    pprint(resp.json()['objectData']['flat']['assignationCode'])
    pprint(resp.json()['objectData']['flat']['area'])
    pprint(resp.json()['objectData']['flat']['cadCostValue'])
    pprint(resp.json()['objectData']['flat']['ccDateEntering'])
    pprint(resp.json()['objectData']['flat']['ccDateValuation'])
    pprint(resp.json()['objectData']['flat']['encumbrancesExists'])
    print()

print('finish')
