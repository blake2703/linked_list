"""
This class will represent the node
    It will have two member variables
        data: the value of the node
        next: the next node
"""
class Node():
    """
    The constructor for the Node class
        @param: data-> null value
        @param: next-> null value
        @return: none
    """
    def __init__(self, data=None, next=None) -> None:
        #set data = data
        self.data = data
        #set next = next
        self.next = next
        