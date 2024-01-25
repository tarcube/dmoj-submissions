def solve(heights):
  n = len(heights)
  values = []
  for length in range(1, n+1):
    min_value = 10**5
    for start in range(n-length+1):
      value = 0
      for i in range(length//2):
        value += abs(heights[start+i] - heights[start+length-1-i])
      if value < min_value:
        min_value = value
    values.append(min_value)
  return values

n = int(input())
heights = list(map(int, input().split()))
values = solve(heights)
output = ""
for i in range(n):
  output += str(values[i]) + " "
print(output[:-1])