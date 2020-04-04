import pdb


def trap(height):
    volumn = 0
    left_max=[]
    right_max=[]
    for i in range(len(height)):
        left_max.append(max(height[0:i+1]))
    for i in range(len(height)):
        right_max.append(max(height[i:]))

    print(left_max)
    print(right_max)

    for i in range(len(height)):
        volumn += min(left_max[i],right_max[i]) - height[i]

    return volumn
        


if __name__=="__main__":
    a_list = [0,1,0,2,1,0,1,3,2,1,2,1]
    rain = trap(a_list)
    print(rain)
