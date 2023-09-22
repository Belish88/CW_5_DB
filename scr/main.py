

from scr.api_hh import HH_VAC, HH_EMP
from scr.setting import HH_VAC_URL, HH_EMP_URL
from scr.utils import search_for_employers, employer_data, company_vacancies


def main():
    name_vac = 'Python'
    area = ['Ульяновск', 'Краснодар']

    list_id_emp = search_for_employers(name_vac, area)
    print(list_id_emp)

    for id_emp in list_id_emp[:20]:
        emp_data = employer_data(id_emp)
        if emp_data[3] < 100:
            print(emp_data)
            print(company_vacancies(id_emp))



    # hh = HH_VAC(name_vac, HH_VAC_URL)
    #
    # page = 0
    # employers = []
    # while not page == 10:
    #     hh.params['page'] = page
    #     page += 1
    #     hh_json = hh.get_request().json()["items"]
    #     # print(hh_json)
    #     for i in hh_json:
    #         if i['area']['name'] in area:
    #             if i['salary']:
    #                 if type(i['salary']['from']) is int and i['salary']['from'] >= 50000:
    #                     employers.append(i['employer']['id'])
    #     #                 print(i['name'],
    #     #                       i['area']['name'],
    #     #                       i['salary']['from'],
    #     #                       i['type']['name'],
    #     #                       i['employer']['name'])
    # vacancies_list_url = []
    # for emp in employers[:1]:
    #     emp_id = emp
    #     url = HH_EMP_URL + emp_id
    #     # print(url)
    #     hh_emp = HH_EMP(url)
    #     e = hh_emp.get_request().json()
    #     vacancies_list_url.append(e['vacancies_url'])
    #     # print(e)
    #     print(e['id'], e['name'], e['area']['name'], e['open_vacancies'], e['alternate_url'])
    #
    # # print(vacancies_list_url)
    #
    # vac_list = []
    # for vac_epm in vacancies_list_url:
    #     hh_vac = HH_VAC(None, vac_epm)
    #     hh_vac_json = hh_vac.get_request().json()["items"]
    #     vac_list.append(hh_vac_json)
    # print(vac_list)
    #
    # for vac_vac in vac_list:
    #     for i in vac_vac:
    #         salary = None
    #         if not i['salary'] == salary:
    #             salary = i['salary']['from']
    #         print(i['id'],
    #               i['employer']['id'],
    #               i['name'],
    #               salary,
    #               i['area']['name'],
    #               i['type']['name'],
    #               i['alternate_url'])

if __name__ == '__main__':
    main()
