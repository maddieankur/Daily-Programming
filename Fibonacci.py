"""
509. Fibonacci Number
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

"""


class Solution:
    def fib(self, N: int) -> int:
        fib = [0]*(N+2)
        fib[0] = 0
        fib[1] = 1
        for i in range(2,N+1,1):
            fib[i] = (fib[i-1]+fib[i-2])
        return fib[N]
