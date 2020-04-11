
def generateParenthesis(n):
    ans = []
    def f(l, r, s):
        l == r == n and ans.append(s)
        l < n and f(l + 1, r, s + '(')
        r < l and f(l, r + 1, s + ')')
    f(0, 0, '')
    return ans


if __name__=="__main__":
    n = 4
    print(generateParenthesis(n))
