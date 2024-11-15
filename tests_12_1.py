import unittest
import runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        """
        Тест функции "walk"
        :return:
        при однократном вызове функции walk, параметр distance увеличивается на значение 5
        """
        r1 = runner.Runner('Объект_1')
        for i in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50)

    def test_run(self):
        """
         Тест функции "run"
         :return:
         при однократном вызове функции run, параметр distance увеличивается на значение 10
         """

        r2 = runner.Runner('Объект_2')
        for i in range(10):
            r2.run()
        self.assertEqual(r2.distance, 100)

    def test_challenge(self):
        """
        Тест функции "challenge"
        :return:
        при однократном вызове функции run, параметр distance увеличивается на значение 10
        """
        r3 = runner.Runner('Объект_3')
        r4 = runner.Runner('Объект_4')
        for i in range(10):
            r3.walk()

        for i in range(10):
            r4.run()
        #print(f'{r3.name} ({r3.distance}) не равен {r4.name} ({r4.distance})')
        self.assertNotEqual(r3.distance, r4.distance)


if __name__ == '__main__':
    unittest.main()
