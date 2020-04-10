#!/usr/bin/env python3

import timeit
import time
import big_o

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

class Solution:
    def middleNodeHareTurtle(self, head: ListNode) -> ListNode:
        # two pointers with hare turtle algo
        hare, turtle = head, head
        while hare and hare.next:
            turtle, hare = turtle.next, hare.next.next
        return turtle

    def middleNodeTraversal(self,head: ListNode) -> ListNode:
        node, c = head, 0
        while node:
            c += 1
            node = node.next
        mid, node = c // 2, head
        for _ in range(mid):
            node = node.next
        return node


def construct_linked_list(linked_list) -> ListNode:
    if len(linked_list) == 0: return

    llist = LinkedList()
    llist.head = ListNode(1)
    # print(f"llist val = {ListNode(1).val}")
    # print(f"llist = {llist.head.val}")
    llist.next = ListNode(linked_list[1])
    # print(f"llist.next = {llist.next.val}")
    llist.next.next = ListNode(linked_list[2])
    # print(f"llist.next.next = {llist.next.next.val}")
    llist.next.next.next = ListNode(linked_list[3])
    # print(f"llist.next.next.next = {llist.next.next.next.val}")
    llist.next.next.next.next = ListNode(linked_list[4])
    # print(f"llist.next.next.next.next = {llist.next.next.next.next.val}")

    # for i in range(1,len(linked_list)):
    #     print(f'index = {i}')
    #     llist.next = ListNode(linked_list[i])
    # llist.next = None
    return llist

llist_vals = [1,2,3,4,5]
llist = construct_linked_list(llist_vals)

# while llist:
#     print(f"current node value: {llist.head.val}")
#     llist = llist.next

s = Solution()
start = time.time()
s.middleNodeHareTurtle(llist)
end = time.time()
print(f'Hare Turtle method takes time: {end - start}')

start = time.time()
s.middleNodeTraversal(llist)
end = time.time()
print(f'Traversal method takes time: {end - start}')

# best_hare_turtle, others_hare_turtle = big_o.big_o(s.middleNodeHareTurtle, llist.head, n_repeats=100)
# best_traversal, others_traversal = big_o.big_o(s.middleNodeTraversal, llist.head, n_repeats=100)
# print(best_hare_turtle)
# print(best_traversal)
