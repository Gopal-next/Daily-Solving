# Some key points on Linked List
'''
Linked list is a data structure that consist of series of nodes connected by pointer or refrences.
Each node cotains data and pointer as a reference.
Linked list is Non-contagious where memory allocated one by one and also having efficient insertion/ deletion.


'''

## Question

'''
[Click Here to See the Question](https://www.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1)
'''

## Add 1 to a Linked List Number



#code

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def addOne(self, head):
        #Returns new head of linked List.
        head = self.reverse(head)

        # Step 2: Add 1 to the reversed list
        carry = 1
        curr = head
        prev = None
        while curr:
            sum_val = curr.data + carry
            carry = sum_val // 10
            curr.data = sum_val % 10
            prev = curr
            curr = curr.next
        
        # If there is still a carry left, add a new node
        if carry:
            prev.next = Node(carry)

        # Step 3: Reverse the list again to restore original order
        head = self.reverse(head)

        return head