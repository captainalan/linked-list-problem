import time
import unittest

from add_two_numbers import ListNode, Solution

"""
Some test case stuff
"""

# Set up the example that we are given
n1 = ListNode(2)
n2 = ListNode(4)
n3 = ListNode(3)

n1.next = n2
n2.next = n3

m1 = ListNode(5)
m2 = ListNode(6)
m3 = ListNode(4)

m1.next = m2
m2.next = m3

# Run the tests
sol = Solution()

# Converting two and from
three = int_to_ListNode(3)
print(ListNode_to_int(three))

thirty_three = int_to_ListNode(33)
print(ListNode_to_int(thirty_three))

print("The example given in this question: ")
print(ListNode_to_int(sol.addTwoNumbers(n1, m1)))


