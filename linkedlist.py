#for my 10years old assignment that I did not finish.

import sys, os

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class LL(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        print new_node.data
        new_node.set_next(self.head)
        print new_node.data
        self.head = new_node
        print self.head.data

#    def size(self):
        
#    def search(self, data):

#    def delete(self, data):

            
    
