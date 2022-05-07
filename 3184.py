boardSize = []
boardSize = input().split()
# print(boardSize)

# board = [[ x for x in input(int(boardSize[0])).split] for y in range(int(boardSize[1]))]

# # print(board)

board = [[x for x in input().split()] for y in range(int(boardSize[0]))]

#우리에 한 종류만 있으면 그대로 count
#우리에 두 종류가 있으면 두 수의 비교 후 count

#우리 안의 갯수를 세는 법

#1 네모 모양
#2 네모 안에 네모: 네모 안에 네모가 있는지
#3 불규칙

#4개로 하면
print(board[0][0])