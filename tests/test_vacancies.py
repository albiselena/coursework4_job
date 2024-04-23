import pytest
from src.vacancies import Vacancies

# Тесты для класса Vacancies

data = [{'name': 'Python Developer',
         'alternate_url': 'https://hh.ru/vacancy/123',
         'snippet': {'requirement': 'Писать код <highlighttext>',
                     'responsibility': 'Писать код <highlighttext>'},
         'area': {'name': 'Москва'},
         'salary': {'from': 100000, 'to': 150000, 'currency': 'руб.'}}]


@pytest.fixture
def vacancies():
    return Vacancies.cast_to_object_list(data)


def test_init(vacancies):
    """Тест __init__ метода класса Vacancies"""
    assert vacancies[0].title == 'Python Developer'
    assert vacancies[0].link == 'https://hh.ru/vacancy/123'
    assert vacancies[0].description == '• Обязанности: Писать код \n• Требования: Писать код '
    assert vacancies[0].city == 'Москва'
    assert vacancies[0].salary == 'от 100000 до 150000 руб.'


def test_salary_output_format():
    """Тест salary_output_format метода"""
    assert Vacancies.salary_output_format(None) == 'Зарплата не указана'
    assert Vacancies.salary_output_format(
        {'from': 100000, 'to': 150000, 'currency': 'руб.'}) == 'от 100000 до 150000 руб.'
    assert Vacancies.salary_output_format({'from': 100000, 'currency': 'руб.'}) == 'от 100000 руб.'
    assert Vacancies.salary_output_format({'to': 150000, 'currency': 'руб.'}) == 'до 150000 руб.'


def test_job_description_format():
    """Тест job_description_format метода"""
    assert Vacancies.job_description_format({'requirement': None,
                                             'responsibility': None}) == '• Описание вакансии отсутствует'
    assert Vacancies.job_description_format({'requirement': 'Ответственный подход к работе<highlighttext>',
                                                'responsibility': 'Ремонт<highlighttext>'}) == (
                '• Обязанности: Ремонт\n'
                '• Требования: Ответственный подход к работе')
    assert Vacancies.job_description_format({'requirement': None,
                                             'responsibility': 'Кодировка<highlighttext>'}) == (
                '• Описание требований отсутствует\n'
                '• Обязанности: Кодировка')
    assert Vacancies.job_description_format({'requirement': 'Управление<highlighttext>',
                                             'responsibility': None}) == (
                '• Описание ответственности отсутствует\n'
                '• Требования: Управление')
