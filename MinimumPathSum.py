import ipdb

def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    arr = [[0 for _ in range(n)] for _ in range(m)]
    arr[0][0] = grid[0][0]

    for i in range(1,n):
        arr[0][i] = grid[0][i] + arr[0][i-1]

    for i in range(1,m):
        arr[i][0] = grid[i][0] + arr[i-1][0]

    for i in range(1,m):
        for j in range(1,n):
            arr[i][j] = min(arr[i-1][j],arr[i][j-1]) + grid[i][j]
    min_sum = arr[m-1][n-1]
    return min_sum



if __name__ == "__main__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    ans = minPathSum(grid)
    print(ans)
