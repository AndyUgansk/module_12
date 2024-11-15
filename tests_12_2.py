from runner_and_tournament import Runner, Tournament
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        result = {}
        for key, value in cls.all_result.items():
            for k, v in value.items():
                result[k] = str(v)
            print(result)

    def test1(self):
        """
        Забег: Усэйн и Ник
        :return:
        """
        first_rase = Tournament(90, self.runner1, self.runner3)
        res = first_rase.start()
        last_runner = list(res.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_result[res.values()] = res

    def test2(self):
        """
        Забег: Андрей и Ник
        :return:
        """
        second_rase = Tournament(90, self.runner2, self.runner3)
        res = second_rase.start()
        last_runner = list(res.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_result[res.values()] = res

    def test3(self):
        """
        Забег: Все трое
        :return:
        """
        third_rase = Tournament(90, self.runner1, self.runner2, self.runner3)
        res = third_rase.start()
        last_runner = list(res.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_result[res.values()] = res


if __name__ == '__main__':
    unittest.main()
