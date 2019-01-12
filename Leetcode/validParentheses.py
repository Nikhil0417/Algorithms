class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stck = []
        count0 = 0
        count1 = 0
        count2 = 0
        try:
            for i in s:
                if i=='(':
                    count0 += 1
                    stck.append(i)
                    print("add")
                elif i=='[':
                    count1 += 1
                    stck.append(i)
                    print("add")
                elif i=='{':
                    count2 += 1
                    stck.append(i)
                    print("add")
                elif i=='}':
                    if(stck.pop()=='{'):
                        count2 -= 1
                        print("del")
                elif i==']':
                    if(stck.pop()=='['):
                        count1 -= 1
                        print("del")
                elif i==')':
                    if(stck.pop()=='('):
                        count0 -= 1
                        print("del")
            print(stck)
        except IndexError:
            return False
        if count0==0 and count1==0 and count2==0:
            return True
        else:
            return False
