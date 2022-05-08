# 45656 수는 인전합 수간의 차이가 1이다. 이런 수를 계단 수라고 한다.
# n이 주어질 때, 길이가 n인 계단 수가 총 몇개인지 구해보자.(0으로 시작하면 계단수 X)
def main():
    n = int(input())
    dp = [[0] * 10 for i in range(n+1)]
    for i in range(1, 10):
        dp[1][i] = i
    for i in range(2, n+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][1]
            elif j == 9:
                dp[i][j] = dp[i-1][8]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    print(sum(dp[n]) % 1000000000)

main()