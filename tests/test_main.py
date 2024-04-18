from main import get_name, get_directory, documents, directories, vote, add, solution
import pytest


class TestPytest():
    # Тест функции возвращающей имя по номеру документа
    def test_get_name(self):
        assert get_name("2207 876234") == "Василий Гупкин"

    # Тест функции возвращающей номер directories по номеру документа
    def test_get_directory(self):
        assert get_directory("2207 876234") == '1'

    # Тест функции добавляющей данные по новому человеку в список documents
    def test_add(self):
        add('international passport', '311 020203', 'Александр Пушкин', 3)
        assert documents[4]['type'] == 'international passport'
        assert documents[4]['number'] == '311 020203'
        assert documents[4]['name'] == 'Александр Пушкин'
        assert directories['3'] == ['311 020203']

    @pytest.mark.parametrize('a, b, c, result', [
        (1, 8, 15, (-3.0, -5.0)),
        (1, -13, 12, (12.0, 1.0)),
        (1, 1, 1, 'корней нет'),
    ])
    # Тест функции для нахождения корней уравнения
    def test_solution(self, a, b, c, result):
        assert solution(a, b, c) == result

    @pytest.mark.parametrize('votes, max_vote', [
        ([1, 1, 1, 2, 3], 1),
        ([1, 2, 3, 2, 2], 2)
    ])
    # Тест функции для нахождения дискриминанта
    def test_vote(self, votes: list, max_vote):
        assert vote(votes) == max_vote