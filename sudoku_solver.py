########################################
# author email: inthra.onsap@gmail.com #
########################################

class SudokuSolver:
    def gridChecker(self, grid):
        if len(grid) != 9:
            return None
        for i in range(9):
            if len(grid[i]) != 9:
                return None
            for j in range(9):
                if (type(grid[i][j]) is not int) or (grid[i][j] < 0) or (grid[i][j] > 9):
                    return None
        return True

    def duplicateChecker(self, grid):
        for c in range(9):
            row_set = set()
            for r in range(9):
                if grid[r][c] != 0:
                    if grid[r][c] in row_set:
                        return True
                    row_set.add(grid[r][c])

        for r in range(9):
            col_set = set()
            for c in range(9):
                if grid[r][c] != 0:
                    if grid[r][c] in col_set:
                        return True
                    col_set.add(grid[r][c])

        for r in range(0, 3):
            for c in range(0, 3):
                subgrid_set = set()
                for rr in range(r * 3, r * 3 + 3):
                    for cc in range(c * 3, c * 3 + 3):
                        if grid[rr][cc] != 0:
                            if grid[rr][cc] in subgrid_set:
                                return True
                            subgrid_set.add(grid[rr][cc])
        return False

    def isValidChecker(self, grid):
        for r in range(9):
            for c in range(9):
                if grid[r][c] == 0:
                    return False
        return True

    def emptyFields(self, grid):
        missing = []
        for r in range(9):
            for c in range(9):
                if grid[r][c] == 0:
                    missing.append((r, c))
        return missing

    def recursiveSolving(self, grid, pos):
        if self.duplicateChecker(grid):
            return False
        if self.isValidChecker(grid):
            return True
        if len(pos) == 0:
            return False

        m_tuple = pos[0]
        for i in range(1, 10):
            grid[m_tuple[0]][m_tuple[1]] = i
            if self.recursiveSolving(grid, pos[1:]):
                return True
        grid[m_tuple[0]][m_tuple[1]] = 0
        return False

    def solve(self, grid):
        if self.gridChecker(grid) is None:
            return None
        return self.recursiveSolving(grid, self.emptyFields(grid)) and grid or False


def main():
    problem_1 = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                 [6, 7, 2, 1, 9, 5, 3, 4, 8],
                 [1, 9, 8, 3, 4, 2, 5, 6, 7],
                 [8, 5, 9, 7, 6, 1, 4, 2, 3],
                 [4, 2, 6, 8, 5, 3, 7, 9, 1],
                 [7, 1, 3, 9, 2, 4, 8, 5, 6],
                 [9, 6, 1, 5, 3, 7, 2, 8, 4],
                 [2, 8, 7, 4, 1, 9, 6, 3, 5],
                 [3, 4, 5, 2, 8, 6, 1, 7, 9]]

    problem_2 = [[2, 9, 0, 0, 0, 0, 0, 7, 0],
                 [3, 0, 6, 0, 0, 8, 4, 0, 0],
                 [8, 0, 0, 0, 4, 0, 0, 0, 2],
                 [0, 2, 0, 0, 3, 1, 0, 0, 7],
                 [0, 0, 0, 0, 8, 0, 0, 0, 0],
                 [1, 0, 0, 9, 5, 0, 0, 6, 0],
                 [7, 0, 0, 0, 9, 0, 0, 0, 1],
                 [0, 0, 1, 2, 0, 0, 3, 0, 6],
                 [0, 3, 0, 0, 0, 0, 0, 5, 9]]

    problem_3 = [[1, 0, 0, 0, 0, 7, 0, 9, 0],
                 [0, 3, 0, 0, 2, 0, 0, 0, 8],
                 [0, 0, 9, 6, 0, 0, 5, 0, 0],
                 [0, 0, 5, 3, 0, 0, 9, 0, 0],
                 [0, 1, 0, 0, 8, 0, 0, 0, 2],
                 [6, 0, 0, 0, 0, 4, 0, 0, 0],
                 [3, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 4, 0, 0, 0, 0, 0, 0, 7],
                 [0, 0, 7, 0, 0, 0, 3, 0, 0]]

    sudokuSolver = SudokuSolver()

    print "Solution 1:"
    solution_1 = sudokuSolver.solve(problem_1)
    for i in range(9):
        print solution_1[i]

    print "\nSolution 2:"
    solution_2 = sudokuSolver.solve(problem_2)
    for i in range(9):
        print solution_2[i]

    print "\nSolution 3:"
    solution_3 = sudokuSolver.solve(problem_3)
    for i in range(9):
        print solution_3[i]

if __name__ == "__main__":
    main()


