"""
Given a reference to the head of a doubly-linked list and an integer, data,
create a new Node object having data value data and insert it into a sorted
linked list.

Complete the Node* SortedInsert(Node* head, int data) method in the editor below.
It has two parameters:
    1. head: A reference to the head of a doubly-linked list of Node objects.
    2. data: An integer denoting the value of the  field for the Node you must
       insert into the list.

The method must insert a new Node into the sorted (in ascending order)
doubly-linked list whose data value is  without breaking any of the list's
double links or causing it to become unsorted.

Note: Recall that an empty list (i.e., where head = null) and a list with one
element are sorted lists.

Input Format
Do not read any input from stdin. Hidden stub code reads in inputs.

Output Format
Do not print anything to stdout. Your method must return a reference to the head
of the same list that was passed to it as a parameter. The custom checker for
this challenge checks the list to ensure it hasn't been modified other than to
properly insert the new Node in the correct location.

"""


class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


def SortedInsert(head, data):
    # make new node with data
    new_node = Node(data)
    # handle edge case of empty list
    if not head:
        return new_node
    # handle edge case if < head data
    elif data <= head.data:
        new_node.next = head
        head.prev = new_node
        return new_node
    # otherwise, traverse the list, recursive call the remaining list
    else:
        remaining = SortedInsert(head.next, data)
        head.next = remaining
        remaining.prev = head
        return head
