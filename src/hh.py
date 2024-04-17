from abc import ABC, abstractmethod
import requests
import pprint


class Parser(ABC):

    @abstractmethod
    def load_vacancies(self, keyword):
        """Метод для загрузки вакансий с платформы"""
        pass


class HeadHunterAPI(Parser):
    """Класс для работы с платформой hh.ru, подключается к API и получает вакансии
    по ключевому слову keyword, который принимается как аргумент в абстрактном классе"""

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.params = {'text': '', 'page': 0, 'per_page': 10}  # per_page стр 100
        self.vacancies = []  # список вакансий

    def load_vacancies(self, keyword):
        self.params['text'] = keyword  # добавляем ключевое слово в параметры запроса
        while self.params.get('page') != 10:  # 20 вакансий на странице
            response = requests.get(self.url, params=self.params)  # делаем запрос
            vacancies = response.json()['items']  # список вакансий
            self.vacancies.extend(vacancies)  # добавляем вакансии в список
            self.params['page'] += 1  # увеличиваем номер страницы
        return self.vacancies


#hh = HeadHunterAPI()

#vv = hh.load_vacancies('програмист')
#pprint.pprint(vv)
