import json
import requests as rq
from pprint import pprint

from .base import Base
from .api import get_cad_data
from .comparator import find_changes


def main():
    base = Base()

    try:
        saved_data = base.open_base()
        print('Cadastre base successful detected!')

        new_data = get_cad_data(saved_data)

        find_changes(saved_data, new_data)

        base.create_base(new_data)

    except IOError:
        print('Cadastre base does not detected! '
              'Trying to find cadastre numbers list.')

        try:
            cad_nums = base.open_list()
            print('Cadastre numbers list detected!')

            new_data = get_cad_data(cad_nums)

            base.create_base(new_data)

        except IOError:
            print('Cadastre numbers list does not detected!')


if __name__ == '__main__':
    main()
