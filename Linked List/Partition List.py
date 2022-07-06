class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def PartitionList(head, x):
    before = before_head = ListNode(-1)
    after = after_head = ListNode(-1)


    curr =head
    while curr:
        if curr.val < x:
            before.next = curr
            before = before.next
        else:
            after.next = curr
            after = after.next
        curr = curr.next

    after.next = None
    before.next = after_head.next
    return before_head.next