#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv, exit

    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)

    try:
        N = int(argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if N < 4:
        print('N must be at least 4')
        exit(1)

    board = [[0] * N for i in range(N)]
    result = []

    def isSafe(x: int, y: int) -> bool:
        """Check if cell board[x][y] is safe to place a queen."""
        # Check this row on left side
        for i in range(y):
            if board[x][i] == 1:
                return False

        # Check upper diagonal on left side
        i = x
        j = y
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Check lower diagonal on left side
        i = x
        j = y
        while j >= 0 and i < N:
            if board[i][j] == 1:
                return False
            i += 1
            j -= 1

        return True

    def solveNQUtil(col: int) -> bool:
        """Recursive utility function to place each queen in a column."""
        global result

        '''Base case: If all queens are placed
        (i.e. reached after the last column),
        then save solution and return true'''
        if col == N:
            sol = []
            for i in range(N):
                for j in range(N):
                    if board[i][j] == 1:
                        sol.append([i, j])
            result.append(sol)
            return True

        # Consider this column and try placing
        # a queen in all rows of that column one by one
        res = False
        for i in range(N):
            if isSafe(i, col):
                board[i][col] = 1
                # Make result true if any placement is possible
                res = solveNQUtil(col + 1) or res
                board[i][col] = 0  # BACKTRACK
        return res

    # start recursion
    solveNQUtil(0)
    for sol in result:
        print(sol)
