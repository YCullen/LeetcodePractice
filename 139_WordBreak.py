import ipdb

class Solution:
    def wordBreak(self, s, worddict):
        n = len(s)
        
        if worddict == []:
            return False

        for i in range(n-1):
            for j in range(i+1,n+1):
                if ((s[i:j] in worddict) and j<n):
                    s = s[j:]
                    return self.wordBreak(s,worddict)
                elif ((s[i:j] in worddict and j==n)):
                    return True
            return False



if __name__=="__main__":
    solution = Solution()
    s = "ab"
    dic = ["a","b"]
    ipdb.set_trace()
    ans = solution.wordBreak(s,dic)
    print(ans)
