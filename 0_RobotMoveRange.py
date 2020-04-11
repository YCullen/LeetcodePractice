import pdb

def movingCount(m,n,k):
    # m,n is less than 100
    # k is less then 20
    def digitSum(num):
        a = num//100
        b = num%100
        c = b//10
        d = b%10
        return a + c + d
    cnt = 1
    attr_mat = [[False for i in range(n)] for j in range(m)]
    attr_mat[0][0] = True
    for i in range(m):
        for j in range(n):
            if i==0 and j==0:
                continue
            if ((i!=0 and attr_mat[i-1][j]) or (j!=0 and attr_mat[i][j-1])) and (digitSum(i) + digitSum(j)) <= k:
                attr_mat[i][j] = True
                cnt = cnt + 1
    return cnt

if __name__ == "__main__":
    m = 16
    n = 8
    k = 4
    print(movingCount(m,n,k))
