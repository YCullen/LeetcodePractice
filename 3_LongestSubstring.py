import ipdb

# 时间10%。内存消耗90%。  运行太慢了 时间复杂度O(n^2)
def lengthOfLongestSubstring(s):
    length = 0
    start = 0
    end = len(s)
    tmp = 0

    if(len(s)==1):
        length = 1
        return length

    while(start<end):
        i = start+1
        while(i<end):
            substring = s[start:i]
            if(s[i] in substring):
                tmp = max(len(substring),tmp)
                break
            elif(i == end-1):
                substring = s[start:]
                tmp = max(len(substring),tmp)
                break
            else:
                i = i + 1
        length = max(tmp,length)
        start = start + 1
    return length

def lengthOfLongestSubstring_2(s):
    if not s:return 0
    left = 0
    lookup = set()
    n = len(s)
    max_len = 0
    cur_len = 0
    for i in range(n):
        cur_len += 1
        while s[i] in lookup:
            lookup.remove(s[left])
            left += 1
            cur_len -= 1
        if cur_len > max_len:max_len = cur_len
        lookup.add(s[i])
    return max_len

if __name__=='__main__':
    s = 'abcb'
    #ipdb.set_trace()
    ans = lengthOfLongestSubstring(s)
    print(ans)
