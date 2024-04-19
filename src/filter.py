#  Функции для фильтрации списка вакансий по городу и зарплате


def filter_city(data):
    """Фильтр списка вакансий по городу,
    функция делает список и возвращает список вакансии по введенному городу пользователем
    для дальнейшей возможной фильтрации"""
    city = input("Введите город для поиска вакансий: ".lower())
    filtered_data = [vacancy for vacancy in data if city in vacancy.city.lower()]
    if filtered_data:
        for vacancy in filtered_data:
            print(vacancy)
        return filtered_data
    else:
        print('Вакансий по данному городу не найдено')


def filter_salary(data):
    """Фильтр списка вакансий по зарплате,
    пользователь вводит зарплату и получает список вакансий с зарплатой больше введенной"""
    minimum_salary = input('Введите минимальную зарплату для поиска вакансий: ')
    sotred_data = []
    for vacancy in data:
        if vacancy.salary == 'Зарплата не указана':
            continue
        salary_from = int(vacancy.salary.split()[1])
        salary_to = int(vacancy.salary.split()[-2])
        if salary_from >= int(minimum_salary):
            sotred_data.append(vacancy)
        if salary_to >= int(minimum_salary):
            sotred_data.append(vacancy)
    if sotred_data:
        for vacancy in sotred_data:
            print(vacancy)
        return sotred_data
