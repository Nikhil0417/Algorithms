class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        #print(emails)
        d = dict() #or d = {}
        answer = []
        for i in range(0,len(emails)):
	        a = emails[i].split('@')
	        #print(a[0])
	        #print(a[1])

	        b = a[0].split('+')
	        #print(b[0])

	        c = b[0].replace('.', "")
	        #print(c)

	        str = c+'@'+a[1]
	        #print(str)

	        if str not in d:
		        d[str] = 1
	        else:
		        d[str] += 1
		        #if d[str] == 2:
			     #   answer.append(str)
	        #print(len(d))
	        #print("**************")

# for j,val in d.items():
# 	if val > 1:
# 		answer.append(j)
# 		print(j,"has appeared more than 1 time")

        #print(answer)
        return len(d)
# return answer
# Add more email IDs in the array
# Remove the debug prints and add the comments
# Try to improvise the complexity
