"""Tests for the Maze class."""

import pytest

from app.maze import Maze

SIMPLE_MAZE = "S..\n###\n..G\n"


def test_maze_from_string(tmp_path):
    """Maze loads correctly from a valid file."""
    maze_file = tmp_path / "maze.txt"
    maze_file.write_text("S..\n...\n..G\n", encoding="utf-8")
    maze = Maze.from_file(maze_file)
    assert maze.start == (0, 0)
    assert maze.goal == (2, 2)
    assert maze.rows == 3
    assert maze.cols == 3


def test_maze_missing_start(tmp_path):
    """ValueError is raised when start is missing."""
    maze_file = tmp_path / "maze.txt"
    maze_file.write_text("...\n...\n..G\n", encoding="utf-8")
    with pytest.raises(ValueError, match="no start"):
        Maze.from_file(maze_file)


def test_maze_missing_goal(tmp_path):
    """ValueError is raised when goal is missing."""
    maze_file = tmp_path / "maze.txt"
    maze_file.write_text("S..\n...\n...\n", encoding="utf-8")
    with pytest.raises(ValueError, match="no goal"):
        Maze.from_file(maze_file)


def test_maze_file_not_found():
    """FileNotFoundError is raised for missing file."""
    with pytest.raises(FileNotFoundError):
        Maze.from_file("/nonexistent/path/maze.txt")


def test_is_walkable(tmp_path):
    """Walls and out-of-bounds cells are not walkable."""
    maze_file = tmp_path / "maze.txt"
    maze_file.write_text("S#G\n", encoding="utf-8")
    maze = Maze.from_file(maze_file)
    assert maze.is_walkable(0, 0) is True   # S
    assert maze.is_walkable(0, 1) is False  # #
    assert maze.is_walkable(0, 2) is True   # G
    assert maze.is_walkable(5, 5) is False  # out of bounds


def test_display_with_path(tmp_path):
    """Display marks inner path cells with *."""
    maze_file = tmp_path / "maze.txt"
    maze_file.write_text("S..G\n", encoding="utf-8")
    maze = Maze.from_file(maze_file)
    result = maze.display([(0, 1), (0, 2)])
    assert "*" in result
