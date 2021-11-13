# 실전 문제 : 1이 될 때까지
# 좀 더 효율적으로 푸는 방법 고민해보기

N, K = map(int, input().split())

cnt = 0

while True:
    if N == 1:
        break
    if N%K == 0:
        N = N//K
    else:
        N -= 1
    cnt += 1

print(cnt)