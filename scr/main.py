from scr.config import config
from scr.db_manager import DBManager
from scr.utils import employers_data, search_for_employers, save_data_to_database, clean_tables


def main():
    do = 0
    while do != 7:
        params = config()
        clean_tables('CW_5_DB', params)
        print('\nИщим компании по названию вакансии и городам')
        name_vac = input('Введите профессию ')
        area = input('Введте города ')

        employer_ids = search_for_employers(name_vac, area)
        data = employers_data(employer_ids[:10])

        save_data_to_database(data, 'CW_5_DB', params)
        dbm = DBManager('CW_5_DB', params)
        print("Компании найдены и добавлены в базу данных")
        while do != 7:
            print("Выберите действие: \n"
                  "1. список всех компаний и количество вакансий.\n"
                  "2. список всех вакансий с указанием названия компании, "
                  "названия вакансии и зарплаты и ссылки на вакансию.\n"
                  "3. средняя зарплата по вакансиям.\n"
                  "4. список всех вакансий, у которых зарплата выше средней по всем вакансиям.\n"
                  "5. список всех вакансий, в названии которых содержатся заданное слово\n"
                  "6. Задать новый поиск компаний\n"
                  "7. Выйти")
            do = int(input('Введите действие: '))

            if do == 1:
                print(dbm.get_companies_and_vacancies_count())
            elif do == 2:
                print(dbm.get_all_vacancies())
            elif do == 3:
                print(dbm.get_avg_salary())
            elif do == 4:
                print(dbm.get_vacancies_with_higher_salary())
            elif do == 5:
                word = input('Введите слово: ')
                print(dbm.get_vacancies_with_keyword(word))
            elif do == 6:
                break
            elif do == 7:
                break

        dbm.cur.close()
        dbm.conn.close()


if __name__ == '__main__':
    main()
