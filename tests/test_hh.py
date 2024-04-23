import unittest
from unittest.mock import patch
from src.hh import HeadHunterAPI

"""Подсмотрела в интернете как тестировать методы класса, который использует requests.get
поэтому не отвечаю за правильность написания теста, но вроде все работает"""


class TestHeadHunterAPI(unittest.TestCase):

        def setUp(self):
            self.hh = HeadHunterAPI()

        @patch('src.hh.requests.get')
        def test_load_vacancies(self, mock_get):
            mock_get.return_value.json.return_value = {'items': [{'name': 'Python Developer'}, {'name': 'Java Developer'}]}
            result = self.hh.load_vacancies('developer')
            self.assertEqual(result, [{'name': 'Python Developer'}, {'name': 'Java Developer'}])


if __name__ == '__main__':
    unittest.main()
