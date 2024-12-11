import time

size = 4

def is_valid_move(x, y, visited):
    """Check if the move is valid (within bounds and not visited)."""
    return 0 <= x < size and 0 <= y < size and (x, y) not in visited

def find_paths(x, y, visited, path, all_paths):
    """Recursive function to find all paths starting from a given node."""
    if len(path) >= 3:
        all_paths.append(path[:])  # Append a copy of the path if it meets the length requirement

    # Define all possible moves (including diagonals)
    moves = [
        (-1, 0), (1, 0), (0, -1), (0, 1),  # Horizontal and vertical
        (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonal
    ]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if is_valid_move(nx, ny, visited):
            visited.add((nx, ny))
            path.append((nx, ny))
            find_paths(nx, ny, visited, path, all_paths)
            path.pop()
            visited.remove((nx, ny))

def all_possible_paths():
    """Find all possible paths in the 4x4 graph."""
    all_paths = []
    cache = {}

    for start_x in range(size):
        for start_y in range(size):
            visited = set()
            visited.add((start_x, start_y))
            start_node = (start_x, start_y)

            if start_node not in cache:
                local_paths = []
                find_paths(start_x, start_y, visited, [start_node], local_paths)
                cache[start_node] = local_paths

            all_paths.extend(cache[start_node])

    return all_paths

# Run the function and print the results
if __name__ == "__main__":
    start = time.time()
    paths = all_possible_paths()
    end = time.time()
    print(f"Total paths: {len(paths)}")
    print(end-start)
    # for path in paths:
    #     print(path)