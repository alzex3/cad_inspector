import json
from deepdiff import DeepDiff


class Base:
    def __init__(self, base_name='cad_base.json', list_name='cad_nums_list.json'):
        self.base_name = base_name
        self.list_name = list_name

    def open_base(self):
        with open(self.base_name, encoding='utf-8') as f:
            return json.load(f)

    def open_list(self):
        with open(self.list_name, encoding='utf-8') as f:
            return json.load(f)

    def create_base(self, cad_data):
        with open(self.base_name, 'w', encoding='utf-8') as f:
            json.dump(cad_data, f, ensure_ascii=False, indent=4)
        print('Cadastre base successful created!')


