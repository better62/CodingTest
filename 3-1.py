# 예제 : 거스름돈

N = int(input("거스름돈 : "))

cnt = 0
for i in [500, 100, 50, 10]:
    cnt += (N//i)
    N %= i

print("거슬러줘야 할 동전의 최소 개수 :", cnt)