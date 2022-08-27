'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

Given an integer n, return a list of two integers [A, B] where:

A and B are No-Zero integers.
A + B = n
The test cases are generated so that there is at least one valid solution. If there are many valid solutions you can return any of them.

 

Example 1:

Input: n = 2
Output: [1,1]
Explanation: A = 1, B = 1. A + B = n and both A and B do not contain any 0 in their decimal representation.
Example 2:

Input: n = 11
Output: [2,9]
 

Constraints:

2 <= n <= 104
'''

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            zero = False
            a = str(i)
            for digit in a:
                if digit == '0':
                    zero = True
                    break
            if zero:
                continue
            b = str(n - i)
            for digit in b:
                if digit == '0':
                    zero = True
                    break
            if zero:
                continue
            return [a, b]