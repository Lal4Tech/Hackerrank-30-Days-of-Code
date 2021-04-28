#!/bin/python3
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Solution():
    def insert(self, head, data):
        node = Node(data)
        if head == None:
            head = node
        else:
            pointer = head
            while pointer.next != None:
                pointer = pointer.next
            pointer.next = node
        return head
    
    def display(self, head):
        pointer = head
        while pointer:
            print(pointer.data, end=' ')
            pointer = pointer.next

if __name__ == '__main__':
    t = int(input())
    head = None
    linked_list = Solution()
    for _ in range(t):
        data = int(input())
        head = linked_list.insert(head, data)

    linked_list.display(head)