def maxArea(height):
    l = len(height)
    left = 0
    right = l-1
    area = 0
    while(left<right):
        if(height[left]<height[right]):
            area = max(area,height[left]*(right-left))
            left=left + 1
        else:
            area = max(area,height[right]*(right-left))
            right = right - 1
    return area

if __name__=='__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height))
