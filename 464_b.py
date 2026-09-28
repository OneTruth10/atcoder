H, W = map(int, input().split())

img = [input() for _ in range(H)]

min_row, max_row = H, -1
min_col, max_col = W, -1

for r in range(H):
    for c in range(W):
        if img[r][c] == '#':
            if r < min_row: min_row = r
            if r > max_row: max_row = r
            if c < min_col: min_col = c
            if c > max_col: max_col = c

for r in range(min_row, max_row + 1):
    print(img[r][min_col : max_col + 1])