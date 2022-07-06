class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        while curr:
            while curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
            curr= curr.next
        return head

    def deleteDuplicates_twopointers(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None or head.next == None):
            return head
        pointer1 = head
        pointer2 = pointer1.next

        while (pointer2 != None):
            if (pointer1.val == pointer2.val):
                pointer1.next = pointer2.next
            else:
                pointer1 = pointer1.next
            pointer2 = pointer1.next

        return head