def count_x_mas(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] != "A":
                continue

            # Diagonal top-left to bottom-right
            diag1 = grid[r-1][c-1] + grid[r][c] + grid[r+1][c+1]
            # Diagonal top-right to bottom-left
            diag2 = grid[r-1][c+1] + grid[r][c] + grid[r+1][c-1]

            if diag1 in ("MAS", "SAM") and diag2 in ("MAS", "SAM"):
                count += 1

    return count


with open("input.txt") as f:
    grid = [line.strip() for line in f]

print(count_x_mas(grid))

# import re
#
# pattern = r"XMAS"
#
#
# # horizontal works 
# def search_word(text):
#     matches = re.findall(pattern, text)
#     return len(matches)
#
#
# with open("input.txt", "r") as file:
#     counter = 0
#     line_stack = []
#     grid = []
#
#     for line in file:
#         line = line.strip()
#         grid.append(line)
#
#         counter += search_word(line)
#         counter += search_word(line[::-1])
#
#         if not line_stack:
#             line_stack = [[] for _ in range(len(line))]
#
#         for i, char in enumerate(line):
#             line_stack[i].append(char)
#
#
#
#     vertical_lines = ["".join(col) for col in line_stack]
#
#     counter += sum([search_word(line) for line in vertical_lines])
#     counter += sum([search_word(line[::-1]) for line in vertical_lines])
#
#
#     rows, cols = len(grid), len(grid[0])
#     diagonals = []
#
#
#     # down right
#     for start_col in range(cols):
#         r, c, diag = 0, start_col, []
#         while r < rows and c < cols:
#             diag.append(grid[r][c])
#             r += 1; c += 1
#
#         diagonals.append("".join(diag))
#
#     for start_row in range(1, rows):
#         r, c, diag = start_row, 0, []
#         while r < rows and c < cols:
#             diag.append(grid[r][c])
#             r += 1; c += 1
#
#         diagonals.append("".join(diag))
#     
#     for start_col in range(cols):
#         r, c, diag = 0, start_col, []
#         while r < rows and c >= 0:
#             diag.append(grid[r][c])
#             r += 1; c -= 1
#
#         diagonals.append("".join(diag))
#
#     for start_row in range(1, rows):
#         r, c, diag = start_row, cols - 1, []
#         while r < rows and c >= 0:
#             diag.append(grid[r][c])
#             r += 1; c -= 1
#
#         diagonals.append("".join(diag))
#             
#
#     counter += sum([search_word(line) for line in diagonals])
#     counter += sum([search_word(line[::-1]) for line in diagonals])
#
#
#     print(counter)
#
#     # print(line_stack)
