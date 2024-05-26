#!/usr/bin/python3
'''7. Singly linked list'''


class Node:
    ''' class Node that defines a node of a singly linked list'''
    def __init__(self, data, next_node=None):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
