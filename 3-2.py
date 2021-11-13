# 실전 문제 : 큰 수의 법칙

N, M, K = map(int, input().split())
List = list(map(int, input().split()))

List.sort()

total = 0
# 두 번째로 큰 수가 더해지는 횟수 구하기
flag = M//(K+1)

# 두 번째로 큰 수 더하기
total += (List[-2]*flag)
# 첫 번째로 큰 수 더하기
total += (List[-1]*(M-flag))

print(total)