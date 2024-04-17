


class Vacancies:
    """Класс для работы с вакансиями"""
    title: str  # название вакансии
    url: str  # ссылка на страницу вакансии
    description: str  # описание вакансии
    city: str  # город
    salary: (int, float, str)  # зарплата вакансии
    currency: str  # валюта

    def __init__(self, title, link, description, city, salary):
        self.title = title
        self.link = link
        self.description = description
        self.city = city
        self.salary = salary

    @staticmethod
    def salary_output_format(salary):
        """Форматирование зарплаты в удобный вид для вывода на экран"""
        if salary is None:
            return 'Зарплата не указана'
        elif isinstance(salary, str):
            return salary
        elif salary.get('from') and salary.get('to'):
            return f'от {salary["from"]} до {salary["to"]} {salary["currency"]}'
        elif salary.get('from'):
            return f'от {salary["from"]} {salary["currency"]}'
        elif salary.get('to'):
            return f'до {salary["to"]} {salary["currency"]}'
        else:
            return 'Зарплата не указана'

    @staticmethod
    def job_description_format(description):
        """Форматирование описания вакансии в удобный вид для вывода на экран"""
        if description.get('responsibility') is None and description.get('requirement') is None:
            return '• Описание вакансии отсутствует'
        if description.get('requirement') and description.get('responsibility'):
            return (
                f'• Обязанности: {description["responsibility"].replace("<highlighttext>", "").replace("</highlighttext>", "")}\n'
                f'• Требования: {description["requirement"].replace("<highlighttext>", "").replace("</highlighttext>", "")}')
        if description.get('requirement') is None:
            return (f'• Описание требований отсутствует\n'
                    f'• Обязанности: {description["responsibility"].replace("<highlighttext>", "").replace("</highlighttext>", "")}')
        if description.get('responsibility') is None:
            return (f'• Описание ответственности отсутствует\n'
                    f'• Требования: {description["requirement"].replace("<highlighttext>", "").replace("</highlighttext>", "")}')

    @classmethod
    def cast_to_object_list(cls, list_vacancy):
        """Конвертация списка словарей в список объектов класса Vacancies"""
        return [cls(vacancy['name'], vacancy['alternate_url'], cls.job_description_format(vacancy['snippet']),
                    vacancy['area']['name'], cls.salary_output_format(vacancy['salary'])) for vacancy in list_vacancy]

    def __gt__(self, other):
        """Переопределение оператора > для сравнения вакансий по зарплате"""
        return self.salary > other.salary

    def __str__(self):
        return (f'Вакансия: {self.title}\n'
                f'Город: {self.city}\n'
                f'Описание требований и обязанностей:\n{self.description}\n'
                f'Зарплата: {self.salary}\n'
                f'Ссылка: {self.link}\n'
                f'\n'
                f'\n')
