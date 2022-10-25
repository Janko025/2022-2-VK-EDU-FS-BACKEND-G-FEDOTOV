from unittest import TestCase, main
from main import CrossZero


class TestCrossZero(TestCase):
    #проверка на комбинацию выиграша
    def test_winner(self):
        winner = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
        self.assertEqual(winner, CrossZero.slip_winner)

    #проверка на количество ячеек поля
    def test_fields(self):
        test_fields = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(test_fields, CrossZero.fields)

if __name__ == '__main__':
    main()



