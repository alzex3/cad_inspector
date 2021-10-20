import requests as rq
import json
from pprint import pprint


def create_cad_base(cad_numbers):
    objects_data = {}
    for number in cad_numbers:

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

    with open('cad_base.json', 'w', encoding='utf-8') as f:
        json.dump(objects_data, f, ensure_ascii=False, indent=4)


def check_cad_base(cad_base):
    objects_data = {}
    for number in cad_base:
        print(number)

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
    # pprint(objects_data)
    pprint(cad_base)

    if objects_data.items() == cad_base.items:
        print('YES')
    else:
        print('Warning!')

    # with open('cad_base.json', 'w', encoding='utf-8') as f:
    #     json.dump(objects_data, f, ensure_ascii=False, indent=4)


try:
    with open('cad_base.json', encoding='utf-8') as f:
        base = json.load(f)
        check_cad_base(base)


except IOError:
    try:
        with open('cad_numbers.txt', encoding='utf-8') as f:
            numbers = []
            for num in f:
                numbers.append(num.strip())
            create_cad_base(numbers)

    except IOError:
        print('File does not exist!')


