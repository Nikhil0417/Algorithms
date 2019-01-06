# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0
        itr = head
        while(itr != None):
            count += 1
            itr = itr.next
        
        mid = int(count/2)+1
        i=0
        while(head!=None):
            i += 1
            if(i==mid):
                break
            head = head.next
        return head
