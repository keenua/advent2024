from typing import List, Tuple, Dict
import heapq


def read_file(file_path: str) -> Tuple[List[List[str]], Tuple[int, int], Tuple[int, int]]:
    with open(file_path, "r") as file:
        grid = [list(line.rstrip('\n')) for line in file]

    start_position = None
    end_position = None

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'S':
                start_position = (i, j)
            elif cell == 'E':
                end_position = (i, j)

    if start_position is None or end_position is None:
        raise ValueError("Start or End position not found in the maze.")

    return grid, start_position, end_position


def compute_min_score(grid: List[List[str]], start_position: Tuple[int, int], end_position: Tuple[int, int]) -> int:
    direction_deltas = {
        'N': (-1, 0),
        'E': (0, 1),
        'S': (1, 0),
        'W': (0, -1)
    }
    left_turn = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
    right_turn = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}

    x_end, y_end = end_position

    heap = []
    heapq.heappush(heap, (manhattan_distance(start_position[0], start_position[1], x_end, y_end), 0, start_position[0], start_position[1], 'E'))

    visited: Dict[Tuple[int, int, str], int] = {}

    while heap:
        estimated_total_cost, total_cost, x, y, direction = heapq.heappop(heap)

        if (x, y) == end_position:
            return total_cost

        state = (x, y, direction)
        if state in visited and visited[state] <= total_cost:
            continue

        visited[state] = total_cost

        # Move forward
        dx, dy = direction_deltas[direction]
        x_new, y_new = x + dx, y + dy
        if 0 <= x_new < len(grid) and 0 <= y_new < len(grid[0]):
            if grid[x_new][y_new] != '#':
                new_total_cost = total_cost + 1
                new_estimated_cost = new_total_cost + manhattan_distance(x_new, y_new, x_end, y_end)
                new_state = (x_new, y_new, direction)
                if new_state not in visited or visited[new_state] > new_total_cost:
                    heapq.heappush(heap, (new_estimated_cost, new_total_cost, x_new, y_new, direction))

        # Rotate left
        new_direction = left_turn[direction]
        new_total_cost = total_cost + 1000
        new_estimated_cost = new_total_cost + manhattan_distance(x, y, x_end, y_end)
        new_state = (x, y, new_direction)
        if new_state not in visited or visited[new_state] > new_total_cost:
            heapq.heappush(heap, (new_estimated_cost, new_total_cost, x, y, new_direction))

        # Rotate right
        new_direction = right_turn[direction]
        new_total_cost = total_cost + 1000
        new_estimated_cost = new_total_cost + manhattan_distance(x, y, x_end, y_end)
        new_state = (x, y, new_direction)
        if new_state not in visited or visited[new_state] > new_total_cost:
            heapq.heappush(heap, (new_estimated_cost, new_total_cost, x, y, new_direction))

    return -1


def manhattan_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


if __name__ == "__main__":
    grid, start_position, end_position = read_file("day16/data.txt")
    min_score = compute_min_score(grid, start_position, end_position)
    print(min_score)