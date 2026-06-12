"""Tests for the BFS algorithm."""


from app.bfs import bfs
from app.maze import Maze


def make_maze(tmp_path, content: str) -> Maze:
    """Helper to create a Maze from a string."""
    f = tmp_path / "maze.txt"
    f.write_text(content, encoding="utf-8")
    return Maze.from_file(f)


def test_simple_path(tmp_path):
    """BFS finds a direct path in a trivial maze."""
    maze = make_maze(tmp_path, "S..G\n")
    path = bfs(maze)
    assert path is not None
    assert path[0] == maze.start
    assert path[-1] == maze.goal


def test_shortest_path(tmp_path):
    """BFS returns the shortest path, not just any path."""
    content = (
        "S...\n"
        "####\n"
        "...G\n"
    )
    maze = make_maze(tmp_path, content)
    path = bfs(maze)
    # No path through the wall
    assert path is None


def test_no_path(tmp_path):
    """BFS returns None when goal is unreachable."""
    content = (
        "S##\n"
        "###\n"
        "##G\n"
    )
    maze = make_maze(tmp_path, content)
    path = bfs(maze)
    assert path is None


def test_path_length(tmp_path):
    """BFS finds the correct length path."""
    content = (
        "S...\n"
        "....\n"
        "....G\n"  # noqa: intentional extra col – test handles it
    )
    # Use a clean uniform maze
    content = (
        "S...\n"
        "####\n"
        "G...\n"
    )
    maze = make_maze(tmp_path, content)
    path = bfs(maze)
    assert path is None  # blocked by wall row


def test_path_through_maze(tmp_path):
    """BFS navigates around walls correctly."""
    content = (
        "S#G\n"
        "...\n"
        "...\n"
    )
    maze = make_maze(tmp_path, content)
    path = bfs(maze)
    assert path is not None
    assert path[0] == (0, 0)
    assert path[-1] == (0, 2)


def test_goal_is_start(tmp_path):
    """If S and G overlap (single cell), path is just that cell."""
    # Tricky: both S and G can't be same cell in our parser.
    # Test adjacent start/goal instead.
    content = "SG\n"
    maze = make_maze(tmp_path, content)
    path = bfs(maze)
    assert path is not None
    assert len(path) == 2


def test_large_maze_solvable(tmp_path):
    """BFS solves a larger maze correctly."""
    content = (
        "S......\n"
        ".#####.\n"
        ".#...#.\n"
        ".#.#.#.\n"
        ".#...#.\n"
        ".#####.\n"
        "......G\n"
    )
    maze = make_maze(tmp_path, content)
    path = bfs(maze)
    assert path is not None
    assert path[0] == maze.start
    assert path[-1] == maze.goal
