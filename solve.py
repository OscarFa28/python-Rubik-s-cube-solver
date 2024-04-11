import heapq

# Define the goal state of the Rubik's Cube
goal_state = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
              [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
              [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
              [[3, 3, 3], [3, 3, 3], [3, 3, 3]],
              [[4, 4, 4], [4, 4, 4], [4, 4, 4]],
              [[5, 5, 5], [5, 5, 5], [5, 5, 5]]]

# Define the initial state of the Rubik's Cube (you can generate a random initial state)
initial_state = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                 [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
                 [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
                 [[3, 3, 3], [3, 3, 3], [3, 3, 3]],
                 [[4, 4, 4], [4, 4, 4], [4, 4, 4]],
                 [[5, 5, 5], [5, 5, 5], [5, 5, 5]]]

# Define possible moves (e.g., clockwise and counterclockwise turns of each face)
possible_moves = [
    lambda cube: rotate_face(cube, 0, 'cw'),  # rotate front face clockwise
    lambda cube: rotate_face(cube, 0, 'ccw'), # rotate front face counterclockwise
    # Repeat similar functions for other faces
]

# Define the heuristic function
def heuristic(state):
    # Simple heuristic: count the number of misplaced cubies
    misplaced = 0
    for layer in state:
        for row in layer:
            for cubie in row:
                if cubie != goal_state[state.index(layer)][layer.index(row)][row.index(cubie)]:
                    misplaced += 1
    return misplaced

# Define the Best-First Search algorithm
def best_first_search(initial_state):
    queue = [(heuristic(initial_state), initial_state)]
    while queue:
        _, state = heapq.heappop(queue)
        if state == goal_state:
            return state
        for move in possible_moves:
            new_state = move(state)
            heapq.heappush(queue, (heuristic(new_state), new_state))

# Define the A* algorithm
def a_star(initial_state):
    queue = [(heuristic(initial_state), 0, initial_state)]
    while queue:
        _, cost, state = heapq.heappop(queue)
        if state == goal_state:
            return state
        for move in possible_moves:
            new_state = move(state)
            new_cost = cost + 1
            heapq.heappush(queue, (heuristic(new_state) + new_cost, new_cost, new_state))
            
#Define the IDA algorithm


# Example usage
# Solve using Best-First Search
result_bfs = best_first_search(initial_state)
print("Best-First Search result:")
print(result_bfs)

# Solve using A*
result_astar = a_star(initial_state)
print("\nA* result:")
print(result_astar)
