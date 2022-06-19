
def permute(a_list):
    ans = []
    def backtrack(nums,tmp):
        if not nums:
            ans.append(tmp)
            return
        for i in range(len(nums)):
            backtrack(nums[:i]+nums[i+1:],tmp + [nums[i]])
    backtrack(a_list,[])
    return ans


if __name__ == '__main__':
    in_list = [1,2,3]
    print(permute(in_list))
    
