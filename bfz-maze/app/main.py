"""Entry point for the BFS Maze Solver."""

import argparse
import sys
import time
from pathlib import Path

from app.bfs import bfs
from app.maze import Maze


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="BFS Maze Solver – finds the shortest path in a text-based maze."
    )
    parser.add_argument(
        "maze_file",
        type=Path,
        help="Path to the maze .txt file (S=start, G=goal, #=wall, .=path)",
    )
    parser.add_argument(
        "--hide-path",
        action="store_true",
        default=False,
        help="Do not display the maze with the solution path marked",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    """Run the BFS maze solver."""
    args = parse_args(argv)

    try:
        maze = Maze.from_file(args.maze_file)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error loading maze: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Maze loaded: {maze.rows} rows × {maze.cols} cols")
    print(f"Start: {maze.start}  |  Goal: {maze.goal}\n")

    start_time = time.perf_counter()
    path = bfs(maze)
    elapsed = time.perf_counter() - start_time

    if path is None:
        print("No path found – the maze has no solution.")
        sys.exit(2)

    # Exclude start and goal from displayed path steps
    inner_path = path[1:-1]

    print(f"Path found! Length: {len(path) - 1} steps  |  Time: {elapsed * 1000:.3f} ms\n")

    if not args.hide_path:
        print(maze.display(inner_path))

    print("\nPath coordinates:")
    print(" -> ".join(str(p) for p in path))


if __name__ == "__main__":
    main()
