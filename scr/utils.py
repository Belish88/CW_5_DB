from scr.api_hh import HH_VAC, HH_EMP
from scr.setting import HH_VAC_URL, HH_EMP_URL


def search_for_employers(name, city):
    """
    Поиск компаний по названию вакансии и городу
    :param name: название вакансии
    :param city: город
    :return: список id компаний
    """
    hh = HH_VAC(name, HH_VAC_URL)
    page = 0
    employers = []
    while not page == 20:
        hh.params['page'] = page
        page += 1
        hh_json = hh.get_request().json()["items"]
        for i in hh_json:
            if i['area']['name'] in city:
                if not i['employer']['id'] in employers:
                    employers.append(i['employer']['id'])
                else:
                    continue
    return employers


def employer_data(id_employer):
    """
    Выводит информацию о компании по ее id
    :param list_id_employers: id компаниb
    :return: информация о компаниb
    """
    url = HH_EMP_URL + id_employer
    hh_emp = HH_EMP(url)
    emp_get = hh_emp.get_request().json()
    return (emp_get['id'],
            emp_get['name'],
            emp_get['area']['name'],
            emp_get['open_vacancies'],
            emp_get['alternate_url'])


def company_vacancies(id_employers):
    # for emp in list_id_employers[:10]:
    url = HH_EMP_URL + id_employers
    hh_emp = HH_EMP(url)
    emp_get = hh_emp.get_request().json()
    vacancies_url = emp_get['vacancies_url']
    hh_vac = HH_VAC(None, vacancies_url)
    hh_vac_json = hh_vac.get_request().json()["items"]
    for vac in hh_vac_json:
        salary = None
        if not vac['salary'] == salary:
            salary = vac['salary']['from']
        return (vac['id'],
                vac['employer']['id'],
                vac['name'],salary,
                vac['area']['name'],
                vac['type']['name'],
                vac['alternate_url'])
