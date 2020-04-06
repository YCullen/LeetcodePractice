import numpy
import pdb

def edit_distance(str1,str2):
    l1 = len(str1)
    l2 = len(str2)
    state_matrix = [[0 for col in range(l2+1)] for row in range(l1+1)]
    for i in range(l1+1):
        state_matrix[i][0] = i
    for i in range(l2+1):
        state_matrix[0][i] = i
    for i in range(l1):
        for j in range(l2):
            if(str1[i]==str2[j]):
                state_matrix[i+1][j+1] = state_matrix[i][j]
            else:
                state_matrix[i+1][j+1] = min(state_matrix[i+1][j], \
                        state_matrix[i][j],state_matrix[i][j+1]) +1
    print(state_matrix)
    return state_matrix[l1][l2]
                

if __name__=="__main__":
    str1 = 'horse'
    str2 = 'ros'
    ans = edit_distance(str1,str2)
    print(ans)
