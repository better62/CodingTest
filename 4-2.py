# 시각
# 책에서는 그냥 삼중 for문 돌렸네..?

N = int(input())

h = 60*60
ms = 15*60*2 - 15*15

if N >= 23:
    final = (3*h + N*ms)
elif N >= 13:
    final = (2*h + N*ms)
elif N >= 3:
    final = (h + N*ms)
else:
    final = N*ms

print(final)