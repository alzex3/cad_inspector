import requests as rq
import json
from pprint import pprint


# cn_numbers = [
#     '52:18:0050135:91',
#     '52:18:0050135:222',
#     '52:18:0050135:11',
#     '52:18:0070179:1083'
# ]


kad_numbers = []
with open('test_kad.txt') as f:
    for number in f:
        kad_numbers.append(number.strip())


objects_data = {}
for number in kad_numbers:

    resp = rq.get(
        url=f'http://rosreestr.ru/fir_lite_rest/api/gkn/fir_lite_object/{number}'
    )

    obj_type = resp.json()['type']
    cn_number = resp.json()['objectCn']
    address = resp.json()['objectData']['address']['mergedAddress']
    cost = 0

    if resp.json()['type'] == 'construction':
        cost = resp.json()['objectData']['construction']['cadCostValue']

    elif resp.json()['type'] == 'flat':
        cost = resp.json()['objectData']['flat']['cadCostValue']

    elif resp.json()['type'] == 'building':
        cost = resp.json()['objectData']['building']['cadCostValue']

    elif resp.json()['type'] == 'parcel':
        cost = resp.json()['objectData']['parcelData']['cadCostValue']

    objects_data[cn_number] = {
        'obj_type': obj_type,
        'address': address,
        'cost': cost
    }

with open('result.txt', 'w', encoding='utf-8') as f:
    json.dump(objects_data, f, ensure_ascii=False)
