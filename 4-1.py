# 상하좌우

N = int(input())
move = list(input().split())

row = 1
col = 1

for i in move:
    if i == 'R' and col < N:
        col += 1
    elif i == 'L' and col > 1:
        col -= 1
    elif i == 'U' and row > 1:
        row -= 1
    elif i == 'D' and row < N:
        row += 1

print(row, col)