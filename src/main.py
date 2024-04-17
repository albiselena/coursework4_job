from src.hh import HeadHunterAPI
from src.vacancies import Vacancies

keyword = input('Введите ключевое слово для поиска вакансий: ')
hh = HeadHunterAPI()
hh_vacancies = hh.load_vacancies(keyword)
vacancies_list = Vacancies.cast_to_object_list(hh_vacancies)

for vacancy in vacancies_list:
    print(vacancy)



