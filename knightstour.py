N = 8

KNIGHT_MOVES = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]


def inside_board(r, c):
    return 0 <= r < N and 0 <= c < N


def is_knight_move(r1, c1, r2, c2):
    return (abs(r1 - r2), abs(c1 - c2)) in [(1, 2), (2, 1)]


def count_degree(board, r, c):
    count = 0
    for dr, dc in KNIGHT_MOVES:
        nr, nc = r + dr, c + dc
        if inside_board(nr, nc) and board[nr][nc] == 0:
            count += 1
    return count


def knights_tour(start_row, start_col, closed=False):
    if not inside_board(start_row, start_col):
        raise ValueError("start di luar papan")

    board = [[0] * N for _ in range(N)]
    path = []
    start = (start_row, start_col)

    def backtrack(r, c, step):
        board[r][c] = step
        path.append((r, c))

        if step == N * N:
            if not closed or is_knight_move(r, c, start[0], start[1]):
                return True
        else:
            candidates = []
            for dr, dc in KNIGHT_MOVES:
                nr, nc = r + dr, c + dc
                if inside_board(nr, nc) and board[nr][nc] == 0:
                    deg = count_degree(board, nr, nc)
                    candidates.append((deg, nr, nc))
            candidates.sort(key=lambda x: x[0])
            for _, nr, nc in candidates:
                if backtrack(nr, nc, step + 1):
                    return True

        board[r][c] = 0
        path.pop()
        return False

    if backtrack(start_row, start_col, 1):
        return board, path
    else:
        return None, None


def print_board(board):
    for row in board:
        print(" ".join(f"{v:2d}" for v in row))


if __name__ == "__main__":
    start_row, start_col = 0, 0
    closed_tour = False

    board, path = knights_tour(start_row, start_col, closed=closed_tour)
    if board is None:
        print("tidak ada solusi")
    else:
        print_board(board)
        print("path:", path)
