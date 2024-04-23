from src.hh import HeadHunterAPI
from src.vacancies import Vacancies
from src.menu import show_all_vacancies, filter_by_city, filter_by_salary, filter_by_city_and_salary, filter_by_keyword, \
    delete_file_json

print('Программа для поиска вакансий на hh.ru')
print('Введите ключевое слово для поиска вакансий:')
keyword = input()
hh = HeadHunterAPI()
hh_vacancies = hh.load_vacancies(keyword)
vacancies_list = Vacancies.cast_to_object_list(hh_vacancies)


def main() -> object:
    while True:
        print('')
        print('1. Показать все вакансии')
        print('2. Фильтрация по городу')
        print('3. Фильтрация по зарплате')
        print('4. Фильтрация по городу и зарплате')
        print('5. Фильтрация по ключевому слову')
        print('6. Хотите очистить существующий файл?')
        print('7. Выход')
        print('Выберите действие:')
        choice = input()
        if choice == '1':
            show_all_vacancies(vacancies_list)
        elif choice == '2':
            filter_by_city(vacancies_list)
        elif choice == '3':
            filter_by_salary(vacancies_list)
        elif choice == '4':
            filter_by_city_and_salary(vacancies_list)
        elif choice == '5':
            filter_by_keyword(vacancies_list)
        elif choice == '6':
            delete_file_json()
        elif choice == '7':
            print('Программа завершена')
            break
        else:
            print('Неверный ввод')


if __name__ == '__main__':
    main()
