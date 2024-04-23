# функции меню для пользователя

from config import ROOT_DIR
import os
from src.class_saver_json import JSONVacancySaver
from src.filter import filter_city, filter_salary, print_filtered_data, filter_jobs_by_keyword

MSG_ENTER_MIN_SALAR = 'Введите минимальную зарплату для поиска вакансий:'
MSG_ENTER_CITY = 'Введите город для поиска вакансий:'
MSG_ENTER_NAME_FILE = 'Введите название файла:'


def show_all_vacancies(vacancies_list):
    """Показать все вакансии из списка или по количеству, введенному пользователем
    привязан к функции main() главное меню кнопка - 1"""
    print('Всего вакансий:', len(vacancies_list))
    print('Сколько вакансий вы хотите увидеть?')
    number_vacancies = int(input())
    for vacancy in vacancies_list[:number_vacancies]:
        print(vacancy)
    edit_or_create_file(vacancies_list[:number_vacancies])


def filter_by_city(vacancies_list):
    """Фильтрация по городу привязан к функции main() главное меню кнопка - 2"""
    print(MSG_ENTER_CITY)
    city = input().lower()
    print_filtered_data(filter_city(vacancies_list, city))
    edit_or_create_file(filter_city(vacancies_list, city))


def filter_by_salary(vacancies_list):
    """Фильтрация по зарплате привязан к функции main() главное меню кнопка - 3"""
    print(MSG_ENTER_MIN_SALAR)
    minimum_salary = int(input())
    print_filtered_data(filter_salary(vacancies_list, minimum_salary))
    edit_or_create_file(filter_salary(vacancies_list, minimum_salary))


def filter_by_city_and_salary(vacancies_list):
    """Фильтрация по городу и зарплате привязан к функции main() главное меню кнопка - 4"""
    print(MSG_ENTER_CITY)
    city = input().lower()
    print(MSG_ENTER_MIN_SALAR)
    minimum_salary = int(input())
    print_filtered_data(filter_salary(filter_city(vacancies_list, city), minimum_salary))
    edit_or_create_file(filter_salary(filter_city(vacancies_list, city), minimum_salary))


def filter_by_keyword(vacancies_list):
    """Фильтрация по ключевому слову привязан к функции main() главное меню кнопка - 5"""
    print('Введите ключевое слово для поиска вакансий:')
    keyword_description = input().lower()
    print_filtered_data(filter_jobs_by_keyword(vacancies_list, keyword_description))
    edit_or_create_file(filter_jobs_by_keyword(vacancies_list, keyword_description))


def edit_or_create_file(vacancies_list):
    """Редактирование или создание файла с вакансиями отображается после фильтрации вакансий,
    как предложение пользователю сохранить вакансии в файл или добавить в уже существующий"""
    print('Хотите сохранить вакансии в файл или добавить в уже существующий?')
    print('1. Сохранить в файл')
    print('2. Добавить в существующий файл')
    print('3. Продолжить поиск')
    user_input = input()
    if user_input == '1':
        print(MSG_ENTER_NAME_FILE)
        filename = input()
        filename = os.path.join(ROOT_DIR, 'data', filename)
        json_saver = JSONVacancySaver(filename)
        json_saver.create_json_file([vacancy.__dict__ for vacancy in vacancies_list])
    elif user_input == '2':
        print(MSG_ENTER_NAME_FILE)
        filename = input()
        filename = os.path.join(ROOT_DIR, 'data', filename)
        json_saver = JSONVacancySaver(filename)
        json_saver.add_vacancies([vacancy.__dict__ for vacancy in vacancies_list])
    elif user_input == '3':
        pass


def get_filename():
    """Получение полного пути к файлу от пользователя"""
    print('Введите название файла:')
    filename = input()
    return os.path.join(ROOT_DIR, 'data', filename)


def delete_file_json():
    """Удаление файла с вакансиями и вывод содержимого файла перед удалением,
    привязан к функции main() главное меню кнопка - 6"""
    filename = get_filename()
    json_saver = JSONVacancySaver(filename)

    while True:
        print('Хотите посмотреть содержимое файла перед удалением?')
        print('1. Да')
        print('2. Нет')
        print('3. Выйти в главное меню')
        user_input = input()

        if user_input == '1':
            print(json_saver.read_vacancies())
            print('Хотите удалить все вакансии из файла?')
            print('1. Да')
            print('2. Нет')
            user_input = input()
            if user_input == '1':
                json_saver.delete_vacancies()
                break
            elif user_input == '2':
                break
        elif user_input == '2':
            json_saver.delete_vacancies()
            break
        elif user_input == '3':
            break
