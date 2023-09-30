import psycopg2

from scr.api_hh import HH_VAC, HH_EMP
from scr.setting import HH_VAC_URL, HH_EMP_URL


def search_for_employers(name, city):
    """
    Поиск компаний по названию вакансии и городу
    :param name: название вакансии
    :param city: город
    :return: список id компаний
    """
    hh = HH_VAC(name, HH_VAC_URL, 10)
    page = 0
    employers_ids = []
    while not page == 20:
        hh.params['page'] = page
        page += 1
        hh_json = hh.get_request().json()["items"]
        for i in hh_json:
            if i['area']['name'] in city:
                if not i['employer']['id'] in employers_ids:
                    employers_ids.append(i['employer']['id'])
                else:
                    continue
    return employers_ids


def employers_data(employer_ids):
    """    Получаем данные о роботадателях и его вакансиях    """

    data = []
    emp_ids = employer_ids

    for emp_id in emp_ids:

        emp_url = HH_EMP_URL + emp_id
        emp_data = HH_EMP(emp_url).get_request().json()

        vacancies_url = emp_data['vacancies_url']
        vacancies_data = HH_VAC(None, vacancies_url, 100).get_request().json()['items']

        data.append({
            'employer': emp_data,
            'vacancies': vacancies_data
        })
    return data


def save_data_to_database(data, database_name, params):

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        for emp in data:
            emp_data = emp['employer']
            cur.execute(
                """
                insert into employers (employer_id, employer_name, employer_city, count_vacancies, employer_url)
                values (%s, %s, %s, %s, %s)
                """,
                (emp_data['id'],
                 emp_data['name'],
                 emp_data['area']['name'],
                 emp_data['open_vacancies'],
                 emp_data['alternate_url'])
            )

            vacancies_data = emp['vacancies']
            for vac in vacancies_data:
                salary = None
                if not vac['salary'] == salary:
                    salary = vac['salary']['from']
                cur.execute(
                    """
                    insert into vacancies 
                    (vacancy_id, employer_id, vacancy_name, salary, city, vacancy_type, vacancy_url)
                    values (%s, %s, %s, %s, %s, %s, %s)
                    """,
                    (vac['id'],
                     emp_data['id'],
                     vac['name'],
                     salary,
                     vac['area']['name'],
                     vac['type']['name'],
                     vac['alternate_url'])
                )
    conn.commit()
    conn.close()


def clean_tables(database_name, params):
    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        cur.execute("truncate table vacancies, employers")

    conn.commit()
    conn.close()
