"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contains a single
digit. Add the two numbers and return it as a linked list.

Example:

    Input: (2 -> 4 -> 3) + (5 -> 6  -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807
"""

# Definition for singly linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    # Helper Functions
    def ListNode_to_int(MyListNode, ten_power=0, current_val=0):
        foo = (MyListNode.val * 10**ten_power)
        if MyListNode.next == None: # Base Case
            return foo + current_val
        else: # Recursive case
            return ListNode_to_int(MyListNode.next, 
                    ten_power+1, current_val+foo) 

def int_to_ListNode(MyInt, prev_node=None):
    foo = mod_ten = MyInt % 10
    bar = ListNode(foo) # Make a new Node

    if MyInt // 10 == 0: # Base case
        bar.next = None # No nodes follow it
        return bar  
    else: # Recursive case
        bar.next = int_to_ListNode(MyInt // 10, bar) # Add node
        return bar


# This is the function we were asked to write in the problem
def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    sum = ListNode_to_int(l1) + ListNode_to_int(l2)
    return int_to_ListNode(sum)

def __init__():
    pass

