class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        g={}
        if len(s)!=len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] in d:
                    d[s[i]]+=1
                else:
                    d[s[i]]=1
                if t[i] in g:
                    g[t[i]]+=1
                else:
                    g[t[i]]=1
            if d == g:
                return True
            else:
                return False