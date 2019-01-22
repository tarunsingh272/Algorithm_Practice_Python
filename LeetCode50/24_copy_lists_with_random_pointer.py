import unittest
from typing import Dict
# Definition for singly-linked list with a random pointer.


class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    # 参考答案
    def __init__(self):
        # Creating a visited dictionary to hold old node reference as "key" and new node reference as the "value"
        self.visited = {}

    def getClonedNode(self, node):
        # If node exists then
        if node:
            # Check if its in the visited dictionary
            if node in self.visited:
                # If its in the visited dictionary then return the new node reference from the dictionary
                return self.visited[node]
            else:
                # Otherwise create a new node, save the reference in the visited dictionary and return it.
                self.visited[node] = RandomListNode(node.label)
                return self.visited[node]
        return None

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if not head:
            return head

        old_node = head
        # Creating the new head node.
        new_node = RandomListNode(old_node.label)
        self.visited[old_node] = new_node

        # Iterate on the linked list until all nodes are cloned.
        while old_node != None:

            # Get the clones of the nodes referenced by random and next pointers.
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)

            # Move one step ahead in the linked list.
            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]


class Solution(object):
    def copyRandomList(self, head):
        """
        这个写法及其巧妙地创建了一个p->q一一对应的字典，
        因此pp = p.random作为输入可以映射到新的linked list中得到qq，即q.random->qq
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        hash_map: Dict[RandomListNode: RandomListNode] = dict()
        p = head
        dummy = RandomListNode(0)
        q = dummy
        while p is not None:
            q.next = RandomListNode(p.label)
            hash_map[p] = q.next
            p = p.next
            q = q.next
        p = head
        q = dummy
        while p is not None:
            q.next.random = hash_map[p.random]
            p = p.next
            q = q.next
        return dummy.next


class Test(unittest.TestCase):
    def test(self):
        head = RandomListNode(0)
        head.next = RandomListNode(1)
        head.random = head.next
        head.next.next = RandomListNode(2)
        head.next.random = head
        head.next.next.random = head.next.next

        p:RandomListNode = Solution().copyRandomList(head)
        self.assertEqual(0, p.label)
        self.assertEqual(1, p.next.label)
        self.assertEqual(2, p.next.next.label)
        self.assertEqual(1, p.random.label)
        self.assertEqual(0, p.random.random.label)
        self.assertEqual(2, p.random.next.random.label)
