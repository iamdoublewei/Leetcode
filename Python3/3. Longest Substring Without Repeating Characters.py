class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        dic = {}
        start = 0
        for i, v in enumerate(s):
            if v in dic and start <= dic[v]:
                start = dic[v] + 1
            else:
                max_len = max(max_len, i - start + 1)
            dic[v] = i
        return max_len