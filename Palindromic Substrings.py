"""
647. Palindromic Substrings
Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        ans = 0
        for center in range(2*N-1):
            left = center//2
            right = left + center%2
            while left >= 0 and right < N and s[left] == s[right]:
                ans+=1
                left-=1
                right+=1
        return ans
        
