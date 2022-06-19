import pdb
def superEggDrop(K,N):
    dp = [0] * (K + 1)
    m = 0
    while dp[K] < N:
        m += 1
        for k in range(K, 0, -1):
            # print(m, k)
            dp[k] = dp[k - 1] + dp[k] + 1
    return m
if __name__ == "__main__":
    K = 3
    N = 14
    print(superEggDrop(K,N))
