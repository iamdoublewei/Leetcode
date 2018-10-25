'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
'''

class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(s, ip, ips):
            if len(ip) == 4:
                if not s: 
                    ips.append('.'.join(ip))
                return
            for i in range(1, 4):
                if not s: return
                if s[0] == '0' and i > 1: return
                if int(s[:i]) > 255: return
                dfs(s[i:], ip + [s[:i]], ips)
            
        ips = []
        dfs(s, [], ips)
        return list(set(ips))