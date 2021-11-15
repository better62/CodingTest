# 왕실의 나이트
# 반복문으로도 풀어보기

where = input()
total = 8

if where[0] in ['a', 'h']:
    total -= 3
elif where[0] in ['b', 'g']:
    total -= 2

if where[1] in ['1', '8']:
    total -= 3
elif where[1] in ['2', '7']:
    total -= 2

print(total)
