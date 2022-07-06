class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def splitListToParts (head, k):

    curr = head
    n = 0
    res = []

    while curr:
        n += 1
        curr = curr.next

    part, left = n//k, n%k
    curr = head
    prev = None
    for _ in range(k):
        res.append(curr)
        for _ in range(part):
            prev = curr
            curr = curr.next
        if left and curr:
            prev = curr
            curr = curr.next
            left -= 1
        if prev:
            prev.next = None
    return res

