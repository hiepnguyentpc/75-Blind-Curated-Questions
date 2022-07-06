class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapNodes( head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        arr = []

        n = 0
        curr = head
        while curr:
            n += 1
            arr.append(curr.val)
            curr = curr.next

        prevHead = ListNode(-1)
        prev = prevHead
        for i in range(len(arr)):
            if prev:
                prev.next = ListNode(arr[i])
            prev = prev.next

        return prevHead.next
