import ipdb

def uniquePaths(m,n):
    num_path = 0
    arr = [[0 for _ in range(m)] for _ in range(n)]
    # 把第一行赋值为1。只有一条路径
    for i in range(m):
        arr[0][i] = 1
    # 把第一列赋值微1，只有一条路径
    for i in range(n):
        arr[i][0] = 1
    # 状态转移：p[i][j] = p[i-1][j] + p[i][j-1]
    for i in range(1,m):
        for j in range(1,n):
            arr[j][i] = arr[j][i-1] + arr[j-1][i]
    return arr[n-1][m-1]

if __name__ == "__main__":
    m = 3
    n = 2
    ipdb.set_trace()
    ans = uniquePaths(m,n)
    print(ans)


