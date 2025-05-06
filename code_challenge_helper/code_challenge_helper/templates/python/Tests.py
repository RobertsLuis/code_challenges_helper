"""
Testes para a resolução do problema: {problem_name}

Data: {date}
"""

import unittest
from Solution import solution


class TestSolution(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(solution(2, 3), 5)
        self.assertEqual(solution(-1, 1), 0)
        self.assertEqual(solution(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
