from scr.config import config
from scr.utils import employers_data, search_for_employers, save_data_to_database


def main():
    name_vac = 'Косметолог' #input('Введите профессию ')
    area = ('Ульяновск', 'Санкт-Петербург', 'Краснодар') #input('Введте город ')

    employer_ids = search_for_employers(name_vac, area)
    data = employers_data(employer_ids[:10])

    # params = config()
    # save_data_to_database(data, 'CW_5_DB', params)


if __name__ == '__main__':
    main()
