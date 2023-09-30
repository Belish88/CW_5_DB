import psycopg2


class DBManager:
    def __init__(self, database_name, params):
        self.conn = psycopg2.connect(dbname=database_name, **params)
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании."""
        self.cur.execute("select employer_name, count_vacancies from employers")
        rows = self.cur.fetchall()
        list_emp_count_vac = []
        for row in rows:
            list_emp_count_vac.append(f'{row[0]}  {row[1]}')
        return list_emp_count_vac

    def get_all_vacancies(self):
        """ получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию."""
        self.cur.execute("""select employer_name, vacancies.vacancy_name, vacancies.salary, vacancies.vacancy_url
                         from employers
                         join vacancies using (employer_id)""")
        rows = self.cur.fetchall()
        list_emp_vac_sal_url = []
        for row in rows:
            list_emp_vac_sal_url.append(f'{row[0]} {row[1]} {row[2]} {row[3]}')
        return list_emp_vac_sal_url

    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям."""
        self.cur.execute("""select avg(salary)
                            from vacancies""")
        avg_salary = int(self.cur.fetchone()[0])
        return avg_salary

    def get_vacancies_with_higher_salary(self):
        """получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""

        self.cur.execute(f"select vacancy_name from vacancies where salary > {self.get_avg_salary()}")
        rows = self.cur.fetchall()
        list_vac = []
        for row in rows:
            list_vac.append(row[0])
        return list_vac

    def get_vacancies_with_keyword(self, word):
        """ получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python"""
        self.cur.execute(f"select vacancy_name from vacancies where vacancy_name like'%{word}%'")
        rows = self.cur.fetchall()
        list_vac = []
        for row in rows:
            list_vac.append(row[0])
        return list_vac
