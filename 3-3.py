# 실전 문제 : 숫자 카드 게임

N, M = map(int, input().split())
card = []

for _ in range(N):
    temp = list(map(int, input().split()))
    card.append(temp)

a = []
for row in range(N):
    temp = card[row]
    a.append(min(temp))

# => row 입력 받을 때 바로 최솟값 검사하는 방법이 더 효율적일듯!

print(max(a))