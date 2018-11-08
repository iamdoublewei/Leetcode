'''
Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:
Input: "x=x"
Output: "Infinite solutions"
Example 3:
Input: "2x=x"
Output: "x=0"
Example 4:
Input: "2x+3x-6x=x+2"
Output: "x=-1"
Example 5:
Input: "x=x+2"
Output: "No solution"
'''

class Solution:
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        x, nums, sign, ops, num = 0, 0, 1, 1, ''
        for s in equation:
            if s == 'x':
                if num:
                    x += ops * sign * int(num)
                else:
                    x += ops * sign * 1
                num = ''
                ops = 1
            elif s in ['-', '+', '=']:
                if num:
                    nums += ops * sign * int(num)
                    num = ''
                    ops = 1
                if s == '-':
                    ops = -1
                if s == '+':
                    ops = 1
                if s == '=':
                    sign = -1
            else:
                num += s
        if num:
            nums += ops * sign * int(num)
        
        if not x and not nums:
            return 'Infinite solutions'
        elif not x:
            return 'No solution'
        else:
            return 'x=' + str(-nums//x)