'''
Given an integer array nums, return the most frequent even element.

If there is a tie, return the smallest one. If there is no such element, return -1.

 

Example 1:

Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.
Example 2:

Input: nums = [4,4,4,9,2,4]
Output: 4
Explanation: 4 is the even element appears the most.
Example 3:

Input: nums = [29,47,21,41,13,37,25,7]
Output: -1
Explanation: There is no even element.
 

Constraints:

1 <= nums.length <= 2000
0 <= nums[i] <= 105
'''

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dic = {}
        frequency = 0
        for num in nums:
            if not num % 2:
                if num in dic:
                    dic[num] += 1
                else:
                    dic[num] = 1
        dic = sorted(list(dic.items()), key=lambda x: (-x[1], x[0]))

        if not len(dic):
            return -1
        else:
            return dic[0][0]