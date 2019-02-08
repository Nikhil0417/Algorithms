# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        tempA = headA
        lenA = 0
        lenB = 0
        while(tempA != None):
            lenA += 1
            tempA = tempA.next
        tempB = headB
        while(tempB != None):
            lenB += 1
            tempB = tempB.next
        if(lenA-lenB>0):
            for i in range(lenA-lenB):
                headA = headA.next
        elif(lenA-lenB<0):
            for i in range(lenB-lenA):
                headB = headB.next
        
        while(headA != None and headB != None):
            print(headA.val, headB.val)
            if(headA==headB):
                return headA
            headA = headA.next
            headB = headB.next
