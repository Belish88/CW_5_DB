create table employers
(
	employer_id int,
	employer_name varchar not null,
	employer_city varchar,
	count_vacancies int,
	employer_url varchar,

	constraint pk_employers_employer_id primary key(employer_id)
);

create table vacancies
(
	vacancy_id int,
	employer_id int,
	vacancy_name varchar,
	salary int,
	city varchar,
	vacancy_type varchar,
	vacancy_url varchar,

	constraint pk_vacancies_vacancy_id primary key(vacancy_id),
	constraint fk_vacancies_employers foreign key(employer_id) references employers(employer_id)
)
