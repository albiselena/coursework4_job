#  Функции для фильтрации списка вакансий по городу и зарплате


def filter_city(data, city):
    """Фильтр списка вакансий по городу"""
    return [vacancy for vacancy in data if city in vacancy.city.lower()]


def filter_salary(data, minimum_salary):
    """Фильтр списка вакансий по зарплате"""
    filtered_salary = []
    for vacancy in data:
        if vacancy.salary == 'Зарплата не указана':
            continue
        salary_parts = vacancy.salary.split()
        salary_length = len(salary_parts)
        if salary_length == 5 and int(salary_parts[1]) <= minimum_salary <= int(salary_parts[-2]):
            filtered_salary.append(vacancy)
        elif salary_length == 3:
            if salary_parts[0] == 'от' and int(salary_parts[1]) <= minimum_salary:
                filtered_salary.append(vacancy)
            if salary_parts[0] == 'до' and int(salary_parts[1]) >= minimum_salary:
                filtered_salary.append(vacancy)
    return filtered_salary


def filter_jobs_by_keyword(data, keyword):
    """Фильтр списка вакансий по ключевому слову"""
    return [vacancy for vacancy in data if keyword in vacancy.description.lower()]


def print_filtered_data(data):
    """Вывод отфильтрованных данных"""
    if data:
        for vacancy in data:
            print(vacancy)
    else:
        print('Вакансии не найдены')
