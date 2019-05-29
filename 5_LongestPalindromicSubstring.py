import ipdb
# Bruce Force
def longestPalindrome(s):
    n = len(s)
    ans_list = []
    for start in range(n):
        for end in range(start+1,n+1):
            if(isPalindrome(s,start,end)):
                ans_list.append(s[start:end])
    return max(ans_list)

def isPalindrome(s,start,end):
    reverse_s = s[start:end][::-1]
    if (len(s[start:end])==1):
        return False
    elif (s[start:end] == reverse_s):
        return True
    else:
        return False




if __name__=="__main__":
    s = "cbbd"
    ipdb.set_trace()
    ans = longestPalindrome(s)
    print(ans)

