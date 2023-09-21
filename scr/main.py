import json

from scr.api_hh import HH, HH_EMP
from scr.setting import HH_VAC_URL, HH_EMP_URL


def main():
    name_vac = 'Python'
    area = ['Ульяновск', 'Санкт-Петербург']
    hh = HH(name_vac, HH_VAC_URL)

    page = 0
    employers = []
    while not page == 10:
        hh.params['page'] = page
        page += 1
        hh_json = hh.get_request().json()["items"]

        for i in hh_json:
            if i['area']['name'] in area:
                if i['salary']:
                    if type(i['salary']['from']) is int and i['salary']['from'] >= 50000:
                        employers.append(i['employer']['id'])
                        # print(i['name'],
                        #       i['area']['name'],
                        #       i['salary']['from'],
                        #       i['type']['name'],
                        #       i['employer']['name'])

    for emp in employers[:8]:
        emp_id = emp
        url = HH_EMP_URL + emp_id
        # print(url)
        hh_emp = HH_EMP(url)
        hh_emp_json = hh_emp.get_request().json()
        print(hh_emp_json)







if __name__ == '__main__':
    main()