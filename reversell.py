"""
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def reverse_ll(head):
        """Given a singly linked list, return its reversed list. """

        # put each node to a new list
        new_list = []
        while head.next:
            new_list.append(head.next.value)
        print(new_list)
        # pop the list from the end to make it a new ll
        reverse_ll = LinkedList()
        while new_list:
            if reverse_ll.head == None:
                new_val = new_list.pop()
                new_node = Node(new_val)
            else:
                new_val = new_list.pop()
                new_node.next = Node(new_val)

        return reverse_ll

# Solutions

def reverseList(head):  # Iterative
    prev, curr = None, head
    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    return prev

def reverseList_v1(head):  # Recursive
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next: # when node is none (1 - 2 - 3 - 4 - 5)
        return head # 5 - none
    p = self.reverseList(head.next)
    head.next.next = head # the outer layer head node (4 - 3 - 2 - 1)
    head.next = None # end one layer of call stack
    return p


