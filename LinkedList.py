

class LinkedList():
    """This will be a class template for a linked list"""
    def __init__(self, data=None, next=None) -> None:
        """Constructor for the linked list
            data will hold the value of the item in the linked list
            next will hold the value of the next item in the linked list
            where next and data are pointers
        """
        self.data = data
        self.next = next
    