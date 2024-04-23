#  Тесты для файла filter.py
#  Проверьте работу функций filter_city, filter_salary и print_filtered_data

import pytest
from src.vacancies import Vacancies
from src.filter import filter_city, filter_salary, print_filtered_data, filter_jobs_by_keyword


@pytest.fixture
def vacancies_list():
    return Vacancies.cast_to_object_list(
        [
            {'name': 'Разработчик', 'alternate_url': 'https://hh.ru/vacancy/1',
             'snippet': {'requirement': 'Фильтр по слову', 'responsibility': 'Обязанности'}, 'area': {'name': 'Москва'},
             'salary': {'from': 70000, 'to': 150000, 'currency': 'RUR'}},
            {'name': 'Разработчик СПБ', 'alternate_url': 'https://hh.ru/vacancy/2',
             'snippet': {'requirement': 'Требования', 'responsibility': 'Хирург в сочи'},
             'area': {'name': 'Санкт-Петербург'}, 'salary': None},
            {'name': 'Разработчик RUR M', 'alternate_url': 'https://hh.ru/vacancy/3',
             'snippet': {'requirement': 'Требования', 'responsibility': 'Обязанности'}, 'area': {'name': 'Москва'},
             'salary': {'from': 80000, 'currency': 'RUR'}},
            {'name': 'Разработчик СПБ', 'alternate_url': 'https://hh.ru/vacancy/4',
             'snippet': {'requirement': 'Требования', 'responsibility': 'Обязанности'},
             'area': {'name': 'Санкт-Петербург'}, 'salary': None},
            {'name': 'Разработчик RUR S', 'alternate_url': 'https://hh.ru/vacancy/5',
             'snippet': {'requirement': 'Фильтр по слову', 'responsibility': 'Обязанности'}, 'area': {'name': 'Сочи'},
             'salary': {'to': 200000, 'currency': 'RUR'}},

        ]
    )


def test_filter_city(vacancies_list, city='москва'):
    """Тестирование фильтрации вакансий по городу"""
    filtered = filter_city(vacancies_list, city)
    assert len(filtered) == 2
    assert all(city in vacancy.city.lower() for vacancy in filtered)
    assert filter_city(vacancies_list, 'сочи') == [vacancies_list[-1]]
    assert filter_city(vacancies_list, 'екатеринбург') == []
    assert filter_city(vacancies_list, 'санкт-петербург') == [vacancies_list[1], vacancies_list[3]]


def test_filter_salary(vacancies_list, minimum_salary=80000):
    """Тестирование фильтрации вакансий по зарплате"""
    filtered = filter_salary(vacancies_list, minimum_salary)
    assert len(filtered) == 3
    assert None not in filtered
    assert all(vacancy.salary != 'Зарплата не указана' for vacancy in filtered)


def test_print_filtered_data(vacancies_list):
    """Тестирование вывода отфильтрованных данных по зарплате"""
    assert print_filtered_data(vacancies_list[:1]) is None
    assert print_filtered_data([]) is None


def test_filter_jobs_by_keyword(vacancies_list, keyword='фильтр'):
    """Тестирование фильтрации вакансий по ключевому слову"""
    filtered = filter_jobs_by_keyword(vacancies_list, keyword)
    assert len(filtered) == 2
    assert all(keyword in vacancy.description.lower() for vacancy in filtered)
    assert filter_jobs_by_keyword(vacancies_list, 'сочи') == [vacancies_list[1]]
