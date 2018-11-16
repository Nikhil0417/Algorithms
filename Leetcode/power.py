def myPow(x,n):
  power=1
  if(n>0):
    power = x*self.myPow(x, n-1)
  else:
    power = 1/(x*self.myPow(x,n+1))
  return power
        
 #compute the power of a given integer without using the inbuilt power function.
