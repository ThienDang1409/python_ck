import heapq

class SudokuNode:
    def __init__(self, puzzle, parent=None):
        self.puzzle = puzzle
        self.parent = parent
        self.g = 0  # Cost to reach the current state
        self.h = self.heuristic()  # Heuristic estimate

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

    def heuristic(self):
        # Heuristic: Count the number of empty cells in the puzzle
        return sum(1 for row in self.puzzle for cell in row if cell == 0)

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.puzzle)
        node = node.parent
    return path[::-1]

def best_first_search_sudoku(initial_state):
    open_set = [SudokuNode(initial_state)]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)

        if all(cell != 0 for row in current_node.puzzle for cell in row):
            return reconstruct_path(current_node)

        closed_set.add(tuple(map(tuple, current_node.puzzle)))

        for neighbor in get_sudoku_neighbors(current_node.puzzle):
            if tuple(map(tuple, neighbor)) in closed_set:
                continue

            neighbor_node = SudokuNode(neighbor, current_node)
            neighbor_node.g = current_node.g + 1

            if neighbor_node not in open_set:
                heapq.heappush(open_set, neighbor_node)

    return None

def get_sudoku_neighbors(board):
    neighbors = []

    # Find the first empty cell
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for digit in range(1, 10):
                    if is_valid_move(board, i, j, digit):
                        new_board = [row[:] for row in board]
                        new_board[i][j] = digit
                        neighbors.append(new_board)
                return neighbors  # Only consider the first empty cell

    return neighbors

def is_valid_move(board, row, col, digit):
    # Check if placing 'digit' at (row, col) is a valid move
    return(
        all(board[row][j] != digit for j in range(9)) and  # Check row
        all(board[i][col] != digit for i in range(9)) and  # Check column
        all(
            board[i][j] != digit
            for i in range(3 * (row // 3), 3 * (row // 3) + 3)
            for j in range(3 * (col // 3), 3 * (col // 3) + 3)
         ) # Check 3x3 box
    )

# Example Usage:
initial_sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

solution_path = best_first_search_sudoku(initial_sudoku_board)

if solution_path:
    print("Solution Found:")
    for step, board in enumerate(solution_path):
        print(f"Step {step + 1}:")
        for row in board:
            print(row)
else:
    print("No solution found.")
