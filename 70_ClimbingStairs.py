import ipdb

# recursion method
def climbStairs(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 3
    else:
        return climbStairs(n-1) + climbStairs(n-2)

# DP method

def climbStairsDP(n):
    if n==1:
        return 1
    if n==2:
        return 2
    
    oneStepBefore = 2
    twoStepBefore = 1
    currentStep = 0
    for i in range(2,n):
        currentStep = oneStepBefore + twoStepBefore
        twoStepBefore = oneStepBefore
        oneStepBefore = currentStep
    return currentStep
    

if __name__=='__main__':
    n =  4 # Number of stairs
    ans = climbStairs(n)
    ans1 = climbStairsDP(n)
    print(ans)
    print(ans1)

