class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        # suggestion: later in a loop for boxes 

        # checking the rows
        for i in range(ROWS):
            r = set()
            for j in range(COLS):
                if board[i][j] != ".":
                    if board[i][j] in r:
                        return False
                    elif board[i][j] not in r:
                        r.add(board[i][j])
        
        # checking the columns
        for j in range(COLS):
            c = set()
            for i in range(ROWS):
                if board[i][j] != ".":
                    if board[i][j] in c:
                        return False
                    elif board[i][j] not in c:
                        c.add(board[i][j])

        # check the boxes
        boxes = defaultdict(list)
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] != ".":
                    if i < 3:
                        if j < 3:
                            boxes[1] += board[i][j]
                        elif j < 6:
                            boxes[2] += board[i][j]
                        else:
                            boxes[3] += board[i][j]
                    elif i < 6: 
                        if j < 3:
                            boxes[4] += board[i][j]
                        elif j < 6:
                            boxes[5] += board[i][j]
                        else:
                            boxes[6] += board[i][j]                    
                    else: 
                        if j < 3:
                            boxes[7] += board[i][j]
                        elif j < 6:
                            boxes[8] += board[i][j]
                        else:
                            boxes[9] += board[i][j]  
        
        for i in range(1, 10):
            if len(boxes[i]) != len((set(boxes[i]))):
                return False

        return True
        