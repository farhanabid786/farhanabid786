from collections import deque

def min_moves_to_reach_destination(M, N, grid, source, destination, move_rule):
    # Directions based on the move rule
    forward = (move_rule[0], move_rule[1])  # Move forward
    right = (move_rule[1], -move_rule[0])   # Move right (90 degree clockwise)
    left = (-move_rule[1], move_rule[0])    # Move left (90 degree anticlockwise)
    backward = (-move_rule[0], -move_rule[1]) # Move backward (180 degrees)
    
    directions = [forward, right, left, backward]
    
    # BFS setup
    queue = deque([(source[0], source[1], 0)])  # (x, y, moves)
    visited = set()
    visited.add(source)
    
    while queue:
        x, y, moves = queue.popleft()
        
        # Check if we reached the destination
        if (x, y) == destination:
            return moves
        
        # Explore all possible directions
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            # Check if the new position is within bounds and is a valid cell
            if 0 <= new_x < M and 0 <= new_y < N and grid[new_x][new_y] == 0 and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, moves + 1))
    
    return -1  # If destination is unreachable

# Example usage for the second input scenario
M, N = 6, 6
grid = [
    [0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 0]
]
source = (0, 0)
destination = (4, 4)
move_rule = (0, 2)

result = min_moves_to_reach_destination(M, N, grid, source, destination, move_rule)
print(result)  # Expected Output: 4