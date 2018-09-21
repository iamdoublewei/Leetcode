'''
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]
 

Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.
'''

#Original straight forward method
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A = A.split()
        B = B.split()
        da = {}
        db = {}
        ua = []
        ub = []
        r = []
        for a in A:
            if a in da:
                da[a] += 1
            else:
                da[a] = 1
        for d in da:
            if da[d] == 1:
                ua.append(d)
        for u in ua:
            if u not in B:
                r.append(u)
        for b in B:
            if b in db:
                db[b] += 1
            else:
                db[b] = 1
        for d in db:
            if db[d] == 1:
                ub.append(d)
        for u in ub:
            if u not in A:
                r.append(u)
        return r
    
# Can be simplify by adding A, B together and find key == 1