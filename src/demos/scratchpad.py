"""
Here we will outline a few concepts in comments and code.
"""


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        new_node = LinkedListNode(data)

        if self.head:
            current = self.head

            while current.next:
                current = current.next

            current.next = new_node
         else:
             self.head = new_node
