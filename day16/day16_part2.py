from typing import List, Tuple, Dict, Set
import heapq


class StateInfo:
    def __init__(self, total_cost: int):
        self.total_cost = total_cost
        self.predecessors: Set[Tuple[int, int, str]] = set()


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


def compute_states_with_min_score(grid: List[List[str]], start_position: Tuple[int, int], end_position: Tuple[int, int]):
    from collections import deque

    directions = ['N', 'E', 'S', 'W']
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
    start_state = (start_position[0], start_position[1], 'E')
    start_total_cost = 0
    heapq.heappush(heap, (manhattan_distance(start_position[0], start_position[1], x_end, y_end), start_total_cost, *start_state))

    states: Dict[Tuple[int, int, str], StateInfo] = {}
    states[start_state] = StateInfo(start_total_cost)

    min_total_cost = None
    end_states = []

    while heap:
        estimated_total_cost, total_cost, x, y, direction = heapq.heappop(heap)

        state = (x, y, direction)

        if (x, y) == end_position:
            if min_total_cost is None or total_cost < min_total_cost:
                min_total_cost = total_cost
                end_states = [state]
            elif total_cost == min_total_cost:
                end_states.append(state)

        current_state_info = states[state]

        dx, dy = direction_deltas[direction]
        x_new, y_new = x + dx, y + dy
        if 0 <= x_new < len(grid) and 0 <= y_new < len(grid[0]):
            if grid[x_new][y_new] != '#':
                new_total_cost = total_cost + 1
                new_state = (x_new, y_new, direction)

                if new_state not in states:
                    states[new_state] = StateInfo(new_total_cost)
                    states[new_state].predecessors.add(state)
                    new_estimated_cost = new_total_cost + manhattan_distance(x_new, y_new, x_end, y_end)
                    heapq.heappush(heap, (new_estimated_cost, new_total_cost, x_new, y_new, direction))
                else:
                    existing_state_info = states[new_state]
                    if new_total_cost < existing_state_info.total_cost:
                        existing_state_info.total_cost = new_total_cost
                        existing_state_info.predecessors = {state}
                        new_estimated_cost = new_total_cost + manhattan_distance(x_new, y_new, x_end, y_end)
                        heapq.heappush(heap, (new_estimated_cost, new_total_cost, x_new, y_new, direction))
                    elif new_total_cost == existing_state_info.total_cost:
                        existing_state_info.predecessors.add(state)

        # Rotate left
        new_direction = left_turn[direction]
        new_total_cost = total_cost + 1000
        new_state = (x, y, new_direction)

        if new_state not in states:
            states[new_state] = StateInfo(new_total_cost)
            states[new_state].predecessors.add(state)
            new_estimated_cost = new_total_cost + manhattan_distance(x, y, x_end, y_end)
            heapq.heappush(heap, (new_estimated_cost, new_total_cost, x, y, new_direction))
        else:
            existing_state_info = states[new_state]
            if new_total_cost < existing_state_info.total_cost:
                existing_state_info.total_cost = new_total_cost
                existing_state_info.predecessors = {state}
                new_estimated_cost = new_total_cost + manhattan_distance(x, y, x_end, y_end)
                heapq.heappush(heap, (new_estimated_cost, new_total_cost, x, y, new_direction))
            elif new_total_cost == existing_state_info.total_cost:
                existing_state_info.predecessors.add(state)

        # Rotate right
        new_direction = right_turn[direction]
        new_total_cost = total_cost + 1000
        new_state = (x, y, new_direction)

        if new_state not in states:
            states[new_state] = StateInfo(new_total_cost)
            states[new_state].predecessors.add(state)
            new_estimated_cost = new_total_cost + manhattan_distance(x, y, x_end, y_end)
            heapq.heappush(heap, (new_estimated_cost, new_total_cost, x, y, new_direction))
        else:
            existing_state_info = states[new_state]
            if new_total_cost < existing_state_info.total_cost:
                existing_state_info.total_cost = new_total_cost
                existing_state_info.predecessors = {state}
                new_estimated_cost = new_total_cost + manhattan_distance(x, y, x_end, y_end)
                heapq.heappush(heap, (new_estimated_cost, new_total_cost, x, y, new_direction))
            elif new_total_cost == existing_state_info.total_cost:
                existing_state_info.predecessors.add(state)

    positions_on_optimal_paths = set()
    visited_backtracking = set()

    optimal_end_states = [state for state in states if (state[0], state[1]) == end_position and states[state].total_cost == min_total_cost]

    if not optimal_end_states:
        return -1, set()

    stack = list(optimal_end_states)

    while stack:
        state = stack.pop()
        if state in visited_backtracking:
            continue
        visited_backtracking.add(state)

        x, y, direction = state
        positions_on_optimal_paths.add((x, y))

        for pred_state in states[state].predecessors:
            stack.append(pred_state)

    return min_total_cost, positions_on_optimal_paths


def manhattan_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


def count_tiles_on_best_paths(file_path: str) -> int:
    grid, start_position, end_position = read_file(file_path)
    min_score, positions_on_optimal_paths = compute_states_with_min_score(grid, start_position, end_position)
    if min_score == -1:
        print("No path found from 'S' to 'E'.")
        return 0
    else:
        return len(positions_on_optimal_paths)


if __name__ == "__main__":
    count = count_tiles_on_best_paths("day16/data.txt")
    print(count)
