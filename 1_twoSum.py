import ipdb

def twoSum(nums,target):
    for i in range(0,len(nums)):
        j = len(nums)-1
        ipdb.set_trace()
        while i<j:
            if nums[i] == target - nums[j]:
                ans = [i,j]
                return ans
            else:
                j = j-1


if __name__=='__main__':
    lst = [3,2,4]
    ipdb.set_trace()
    ans = twoSum(lst,6)
    ans = twoSum(lst,7)
    print(ans)