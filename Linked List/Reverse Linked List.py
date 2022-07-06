class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseListIterative(head):
    prev, curr = None, head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev

def reverseListRecursive(head):
    if not head:
        return None
    newHead = head
    if head.next:
        newHead = reverseListRecursive(head.next)
        head.next.next = head
    head.next = None
    return newHead