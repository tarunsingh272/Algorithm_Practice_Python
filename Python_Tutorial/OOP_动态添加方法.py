"""
https://rszalski.github.io/magicmethods/#operators
__cmp__(self, other)
__cmp__ is the most basic of the comparison magic methods. It actually implements behavior for all of the comparison
operators (<, ==, !=, etc.), but it might not do it the way you want (for example, i
f whether one instance was equal to another were determined by one criterion and and whether an instance is greater
than another were determined by something else). __cmp__ should return a negative integer if self < other,
zero if self == other, and positive if self > other. It's usually best to define each comparison you need rather
than define them all at once, but __cmp__ can be a good way to save repetition and improve clarity when you need all
comparisons implemented with similar criteria.
__eq__(self, other)
Defines behavior for the equality operator, ==.
__ne__(self, other)
Defines behavior for the inequality operator, !=.
__lt__(self, other)
Defines behavior for the less-than operator, <.
__gt__(self, other)
Defines behavior for the greater-than operator, >.
__le__(self, other)
Defines behavior for the less-than-or-equal-to operator, <=.
__ge__(self, other)
Defines behavior for the greater-than-or-equal-to operator, >=.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def less_than(self, other):
    return self.val < other.val


ListNode.__lt__ = less_than

node1 = ListNode(1)
node2 = ListNode(2)
print(node1 < node2)
