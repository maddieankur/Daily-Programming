"""
209. Minimum Size Subarray Sum
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 




"""



import math

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i,j = 0,0
        mx = math.inf
        sm = 0
        while(j<len(nums)):
            sm+=nums[j]
            while sm>=s:
                mx = min(mx,j-i+1)
                sm-=nums[i]
                i+=1
            j+=1
        return mx if mx != math.inf else 0
        
