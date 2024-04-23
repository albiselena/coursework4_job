from abc import ABC, abstractmethod
import json
import os
from config import ROOT_DIR

# Путь к файлу для сохранения вакансий
operation_path = os.path.join(ROOT_DIR, 'data')


class AbstractVacancySaver(ABC):
    @abstractmethod
    def create_json_file(self, vacancies):
        pass

    @abstractmethod
    def add_vacancies(self, vacancies):
        pass

    @abstractmethod
    def read_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass

    @abstractmethod
    def get_vacancies_by_criteria(self, criteria):
        pass


class JSONVacancySaver(AbstractVacancySaver):
    def __init__(self, filename):
        self.filename = os.path.join(operation_path, filename) + '.json'

    def create_json_file(self, vacancies):
        """Создание json файла с вакансиями"""
        with open(self.filename, 'w') as file:
            json.dump(vacancies, file, indent=4, ensure_ascii=False)
        print(f'Файл создан {self.filename}')

    def add_vacancies(self, vacancies):
        """Добавление вакансий в файл"""
        with open(self.filename, 'r+') as file:
            data = json.load(file)
            data.extend(vacancies)
            file.seek(0)
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f'Вакансии добавлены в файл {self.filename}')

    def read_vacancies(self):
        """Чтение вакансий из файла"""
        print(f'Чтение вакансий из файла {self.filename}')
        with open(self.filename, 'r') as file:
            data = json.load(file)
        return data

    def delete_vacancies(self):
        """Удаление всех вакансий из файла"""
        with open(self.filename, 'w') as file:
            json.dump([], file, indent=4, ensure_ascii=False)
        print(f'Файл {self.filename} очищен')

    def get_vacancies_by_criteria(self, criteria):
        """Получение вакансий по критерию"""
        #with open(self.filename, 'r') as file:
            #data = json.load(file)
            #return [vacancy for vacancy in data if criteria in vacancy.values()]
        pass
