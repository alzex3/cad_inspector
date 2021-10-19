# for number in kad_numbers:
#     resp = rq.get(url=f'https://rosreestr.ru/fir_rest/api/fir/fir_objects/{number}')
#     for i in resp.json():
#         resp_2 = rq.get(url=f'https://rosreestr.ru/fir_rest/api/fir/fir_objects/152_136162031')
#         pprint(i["objectId"])
#     # pprint(resp.json()["objectId"])


# resp_2 = rq.get(url=f'https://rosreestr.ru/fir_rest/api/fir/fir_object/152_136162031')
# pprint(resp_2.json())