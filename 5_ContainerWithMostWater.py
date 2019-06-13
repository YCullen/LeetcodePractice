import ipdb

def maxArea(height):
    maxArea = 0
    n = len(height)
    
    for i in range(n-1):
        for j in range (i+1,n):
            area = min(height[i],height[j]) * (j-i)
            maxArea = max(area,maxArea)
    return maxArea

def maxArea_twoPointer(height):
    maxArea = 0
    i = 0
    j = len(height) - 1 
    while (i<j):
        area = min(height[i],height[j]) * (j-i)
        if (height[i]<height[j]):
            i += 1
        else:
            j -= 1
        maxArea = max(area,maxArea)
    return maxArea

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    ans = maxArea_twoPointer(height)
    print(ans)
