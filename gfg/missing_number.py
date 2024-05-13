"""Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element."""

class Solution:
    def missingNumber(self,array,n):
        num_set=set(array)
        for i in range(1,n+1):
            if i not in num_set:
               return i
            

obj = Solution()

result = obj.missingNumber([1,3,5,4],4)

print(result)