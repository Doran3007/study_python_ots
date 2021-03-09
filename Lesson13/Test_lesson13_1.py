from unittest import TestCase
from Lesson13_1 import Solver, mul
from pytest import mark


@mark.parametrize(
    "values, expected_res",
    [
        ((3, 5), 15),
        ((1, 10), 10),
        ((1, 0), 0),
        ((4, 8), 32)
    ]
)
def test_mul(values, expected_res):
    res = mul(*values)
    assert res == expected_res

# class TestSolver(TestCase):
#     def test_add(self):
#         res = Solver.add(1, 2)
#         self.assertEqual(res, 3)
#
#         res = Solver.add(4, 5)
#         self.assertEqual(res, 9)
