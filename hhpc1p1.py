# python fast io
import sys
input = sys.stdin.readline

for _ in range(int(input())):
  n = int(input())
  s = input()
  # sliding window
  start, end, maxLen, maxCount = 0, 0, 0, 0
  freq = {}
  while end < n:
    # set default return to 0 if key not found
    freq[s[end]] = freq.get(s[end],0)+1
    maxCount = max(maxCount, freq[s[end]])
    if (end-start+1)-maxCount > 1:
      freq[s[start]] -= 1
      start += 1
    maxLen = max(maxLen, end-start+1)
    end += 1

  sys.stdout.write(str(maxLen)+"\n")