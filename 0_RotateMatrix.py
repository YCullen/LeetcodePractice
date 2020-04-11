import pdb


def rotate(matrix):
    # 矩阵转90度的本质是把第i行换到第-i列
    N = len(matrix)
    matrix_copy = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            matrix_copy[i][j] = matrix[i][j]
    for i in range(N):
        tmp = matrix_copy[i]
        for j in range(N):
            matrix[j][N-1-i] = tmp[j]
    return matrix

if __name__ == "__main__":
    matrix = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    ans = rotate(matrix)
    print(ans)
