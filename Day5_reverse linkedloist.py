# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        curr = head
        count = 0

        # Check if there are at least k nodes
        while curr and count < k:
            curr = curr.next
            count += 1

        # If nodes are less than k, return as it is
        if count < k:
            return head

        # Reverse first k nodes
        prev = None
        curr = head

        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Recursive call for remaining nodes
        head.next = self.reverseKGroup(curr, k)

        return prev


# Helper Functions
def create_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next



arr = [1, 2, 3, 4, 5]
k = 2

head = create_linked_list(arr)

sol = Solution()
new_head = sol.reverseKGroup(head, k)

print("Reversed in K Group:")
print_linked_list(new_head)
