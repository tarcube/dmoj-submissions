# attempt to solve this without 2d arrays

n = int(input())
m = int(input())

coords = {}
x, y = 0, 0
directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
num = n
dir_idx = 0
step = 0
while num <= m:
  for i in range(2):
    for j in range(step):
      if num > m:
        break
      coords[(x, y)] = num
      num += 1
      dx, dy = directions[dir_idx]
      x += dx
      y += dy
    dir_idx = (dir_idx + 1) % 4
  step += 1

min_x = min(x for x, y in coords)
max_x = max(x for x, y in coords)
min_y = min(y for x, y in coords)
max_y = max(y for x, y in coords)
for y in range(min_y, max_y + 1):
  for x in range(min_x, max_x + 1):
    print(coords.get((x, y), ' '), end=' ')
  print("\n", end='')