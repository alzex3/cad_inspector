import requests as rq
from pprint import pprint
import json

number = '52:18:0050135:359'

resp = rq.get(url=f'http://rosreestr.ru/fir_lite_rest/api/gkn/fir_lite_object/{number}', verify=False)
resp2 = rq.get(url=f'https://rosreestr.ru/fir_rest/api/fir/fir_egrp_object/152_6963608000', verify=False)
resp3 = rq.get(url=f'https://rosreestr.ru/fir_rest/api/fir/fir_objects/{number}', verify=False)
resp4 = rq.get(url=f'https://rosreestr.ru/fir_rest/api/fir/fir_object/152_6963608000', verify=False)


print('resp1')
pprint(resp.json())
print('resp2')
pprint(resp2.json())
print('resp3')
pprint(resp3.json())
print('resp')
pprint(resp4.json())