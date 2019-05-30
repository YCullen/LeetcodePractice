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


# Dynamic Programming
def longestPalindrome_2(s):
    n = len(s)
    Pij = [[False for _ in range(n)] for _ in range(n)]

    max_len = 0
    substring = (0,0)

    # one character case
    for i in range(n):
        Pij[i][i] = True

    # two character case
    for i in range(n-1):
        Pij[i][i+1] = s[i]==s[i+1]
        if Pij[i][i+1]:
            if (max_len<2):
                max_len = 2
                substring = (i,i+1)
    
    # more characters case
    step = 2
    for _ in range(n-2):
        i = 0
        j = i+step
        while (i<n-2 and j<n):
            Pij[i][j] = Pij[i+1][j-1] and s[i]==s[j]
            if (Pij[i][j] and (max_len < j-i+1)):
                max_len = j-i+1
                substring = (i,j)
            i+=1
            j+=1
        step+=1

    return s[substring[0]:substring[1]+1]



if __name__=="__main__":
    s = "abcba"
    ipdb.set_trace()
    ans = longestPalindrome_2(s)
    print(ans)

