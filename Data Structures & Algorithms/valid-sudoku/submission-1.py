class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # cols = defaultdict(set)
        # rows = defaultdict(set)
        # squares = defaultdict(set)

        # for r in range(9):
        #     for c in range(9):
        #         if board[r][c] == ".":
        #             continue
        #         if ( board[r][c] in rows[r]
        #             or board[r][c] in cols[c]
        #             or board[r][c] in squares[(r // 3, c // 3)]):
        #             return False

        #         cols[c].add(board[r][c])
        #         rows[r].add(board[r][c])
        #         squares[(r // 3, c // 3)].add(board[r][c])

        # return True

        # non default list solution
        colDict = {}
        rowDict, squareDict = {},{}

        for i, row in enumerate(board):

            for j, val in enumerate(row):
                squareNo = 3 * (i // 3) + j//3
                if val == "." :
                    continue
                if j not in colDict:
                    colDict[j] = set()
                if i not in rowDict:
                    rowDict[i]= set()
                if squareNo not in squareDict:
                    squareDict[squareNo] = set()
                if val in colDict[j] or val in rowDict[i] or val in squareDict[squareNo]:
                    return False
                colDict[j].add(val)
                rowDict[i].add(val)
                squareDict[squareNo].add(val)
        return True