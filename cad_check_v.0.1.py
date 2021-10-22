import requests as rq
import json
from pprint import pprint
from deepdiff import DeepDiff


def get_cad_data(cad_numbers):
    objects_data = {}
    for number in cad_numbers:

        resp = rq.get(
            url=f'http://rosreestr.ru/fir_lite_rest/api/gkn/fir_lite_object/{number}'
        )

        obj_type = resp.json()['type']
        if resp.json()['type'] == 'parcel':
            obj_type = 'parcelData'

        objects_data[resp.json()['objectCn']] = {
            'obj_type': obj_type,
            'address': resp.json()['objectData']['address']['mergedAddress'],
            'update_date': resp.json()['objectData'][obj_type]['actualDate'],
            'full_address': resp.json()['objectData']['address']['note'],
            'created_date': resp.json()['objectData']['dateCreated'],
            'cad_date': resp.json()['objectData']['dateCreated'],
            'cost': resp.json()['objectData'][obj_type]['cadCostValue'],
        }

    return objects_data


def create_cad_base(numbers):
    with open('cad_base.json', 'w', encoding='utf-8') as f:
        json.dump(get_cad_data(numbers), f, ensure_ascii=False, indent=4)
    print('Cadastre base successful created!')


def check_cad_base(cad_base):
    objects_data = get_cad_data(cad_base)
    if DeepDiff(objects_data, cad_base):
        print('New data detected!')
        pprint(DeepDiff(objects_data, cad_base))
        with open('cad_base.json', 'w', encoding='utf-8') as f:
            json.dump(objects_data, f, ensure_ascii=False, indent=4)
            print('New data successful saved to base!')
    else:
        print('Saved data is up to date!')


def main():
    try:
        with open('cad_base.json', encoding='utf-8') as f:
            print('Cadastre base successful detected!')
            check_cad_base(json.load(f))
    except IOError:
        print('Cadastre base does not detected! '
              'Trying to find cadastre numbers list.')
        try:
            with open('cad_numbers.json', encoding='utf-8') as f:
                print('Cadastre numbers list detected!')
                create_cad_base(json.load(f))
        except IOError:
            print('Cadastre numbers list does not detected!')


main()
