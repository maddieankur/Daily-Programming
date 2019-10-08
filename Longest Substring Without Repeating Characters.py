"""
3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.
Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ":
            return 1
        maxCount,maxLen,i,j=0,0,0,0
        window = [0]*256
        while(j<len(s)):
            idx = ord(s[j])-ord('a')
            window[idx]+=1
            maxCount = max(maxCount,window[idx])
            while maxCount > 1:
                window[ord(s[i])-ord('a')]-=1
                maxCount= max(window)
                i+=1
            maxLen = max(maxLen,j-i+1)
            j+=1
        return maxLen
        
