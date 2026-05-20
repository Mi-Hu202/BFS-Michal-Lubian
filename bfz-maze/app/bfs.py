"""BFS (Breadth-First Search) algorithm for finding the shortest path in a maze."""

from collections import deque

from app.maze import Maze


DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(maze: Maze) -> list[tuple[int, int]] | None:
    """Find the shortest path from start to goal using BFS.

    The algorithm explores the maze level by level (row by row in terms of
    distance), which guarantees that the first path found to the goal is
    the shortest one.

    Args:
        maze: A Maze instance with a valid start and goal.

    Returns:
        A list of (row, col) tuples representing the path from start to goal
        (inclusive), or None if no path exists.
    """
    start = maze.start
    goal = maze.goal

    # Queue holds (current_position, path_so_far)
    queue: deque[tuple[tuple[int, int], list[tuple[int, int]]]] = deque()
    queue.append((start, [start]))

    visited: set[tuple[int, int]] = {start}

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path

        row, col = current
        for dr, dc in DIRECTIONS:
            neighbor = (row + dr, col + dc)
            nr, nc = neighbor

            if neighbor not in visited and maze.is_walkable(nr, nc):
                visited.add(neighbor)
                queue.append((neighbor, [*path, neighbor]))

    return None
