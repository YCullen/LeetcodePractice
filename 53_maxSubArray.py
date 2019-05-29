import ipdb
import numpy as np

def maxSubArray(nums):
    n = len(nums)
    for i in range(1,n):
        if nums[i-1]>0:
            nums[i] += nums[i-1]
    return max(nums)


if __name__=='__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))
    