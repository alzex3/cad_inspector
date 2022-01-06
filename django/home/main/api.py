import json
import requests as rq
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_cad_data(number):
    object_data = {}
    resp = rq.get(
        url=f'http://rosreestr.ru/fir_lite_rest/api/gkn/fir_lite_object/{number}',
        verify=False,
    ).json()

    obj_type = resp['type']
    if resp['type'] == 'parcel':
        obj_type = 'parcelData'

    object_data[resp['objectCn']] = {
        'obj_type': obj_type,
        'address': resp['objectData']['address']['mergedAddress'],
        'update_date': resp['objectData'][obj_type]['actualDate'],
        'full_address': resp['objectData']['address']['note'],
        'created_date': resp['objectData']['dateCreated'],
        'cost': resp['objectData'][obj_type]['cadCostValue'],
    }

    return object_data
