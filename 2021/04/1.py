with open("input.txt") as file: lines = file.read().splitlines()

numbers = list(map(int,lines[0].split(",")))

boardSize=5
boards=[]
board=[]
for i in range(2, len(lines)):
    line = lines[i]
    if line=="":
        boards.append(board)
        board=[]
        continue
    board.append(list(map(int,line.split())))
boards.append(board)

def IsBingo(board, row, colunm):
    return all(n == "X" for n in board[row]) or  all(board[i][colunm] =="X" for i in range(boardSize))

def playBingo(numbers, boards):
    for n in numbers:
        #print(n)

        for b in boards:
            #print("checking board...")
            for i in range(boardSize):
                if (n in b[i]):
                    #print("Found a ", n)
                    numIndex = b[i].index(n)
                    b[i][numIndex] = "X"
                    if (IsBingo(b, i, numIndex)):
                        print("BINGO!")
                        return b, n

winnerBoard, finalNum = playBingo(numbers, boards)

print(winnerBoard)
print(finalNum)

soma = 0
for row in winnerBoard:
    for num in row:
        if num!="X":
            soma+=num
print(soma)
print(finalNum*soma)


                