import unittest
from add_two_numbers import * # Just testing one small file!

"""For testing that ListNodes <-> int Conversions work"""
three = int_to_ListNode(3)
thirty_three = int_to_ListNode(33)

"""Set up the example that we are given"""
# 342
n1 = ListNode(2)
n2 = ListNode(4)
n3 = ListNode(3)
n1.next = n2
n2.next = n3

# 465
m1 = ListNode(5)
m2 = ListNode(6)
m3 = ListNode(4)
m1.next = m2
m2.next = m3

class MyTest(unittest.TestCase):
    """
    Tests

    Example input/output from problem statement reproduced here.

    Input: (2 -> 4 -> 3) + (5 -> 6  -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807
    """

    def test_one_digit(self):
        self.assertEqual(ListNode_to_int(three), 3)

    def test_two_digits(self):
        self.assertEqual(ListNode_to_int(thirty_three), 33)

    def test_three_digits(self):
        self.assertEqual(ListNode_to_int(n1), 342)
        self.assertEqual(ListNode_to_int(m1), 465)

    def test_adding_solution(self):
        sol = Solution()
        # Example from problem statement
        self.assertEqual(ListNode_to_int(sol.addTwoNumbers(n1, m1)), 807)

        # Some bigger numbers
        over9000_1 = ListNode(123456789)
        over9000_2 = ListNode(987654321)
        self.assertEqual(ListNode_to_int(sol.addTwoNumbers(over9000_1,
            over9000_2)), (123456789 + 987654321))

if __name__ == '__main__':
    unittest.main()
