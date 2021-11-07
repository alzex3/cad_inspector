import json

# with open('cad_nums.txt', 'r', encoding='utf-8') as f:
#     for i in f:
#         with open('cad_numsss.json', 'a', encoding='utf-8') as file:
#             json.dump(i, file, ensure_ascii=False, indent=4)


with open('cad_numsss.json', encoding='utf-8') as file:
    print(json.load(file))
