# 10/100 IR 1pp
n = int(input())
board = [[0 for i in range(n)] for i in range(n)]
#
for i in range(n//5+1):
    board[4*i+2] = [1 for i in range(n)]
#
for i in range(n):
    a = ""
    for j in range(n):
        a += str(board[i][j]) + " "
    print(a[0:-1])