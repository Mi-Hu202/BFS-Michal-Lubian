"""Maze representation and loading from text files."""

from dataclasses import dataclass, field
from pathlib import Path

WALL = "#"
PATH = "."
START = "S"
GOAL = "G"
VALID_CHARS = {WALL, PATH, START, GOAL}


def _parse_row(line: str, row_idx: int) -> tuple[list[str], tuple[int, int] | None, tuple[int, int] | None]:
    """Parse a single maze row and return (cells, start_pos, goal_pos)."""
    row = list(line)
    start = None
    goal = None
    for col_idx, cell in enumerate(row):
        if cell == START:
            start = (row_idx, col_idx)
        elif cell == GOAL:
            goal = (row_idx, col_idx)
        elif cell not in VALID_CHARS:
            raise ValueError(f"Unknown character '{cell}' at ({row_idx}, {col_idx})")
    return row, start, goal


def _validate_grid(grid: list[list[str]], start: tuple[int, int] | None, goal: tuple[int, int] | None) -> None:
    """Validate the fully parsed grid."""
    if not grid:
        raise ValueError("Maze file is empty.")
    if start is None:
        raise ValueError("Maze has no start position (S).")
    if goal is None:
        raise ValueError("Maze has no goal position (G).")
    cols = len(grid[0])
    for i, row in enumerate(grid):
        if len(row) != cols:
            raise ValueError(f"Row {i} has inconsistent length.")


@dataclass
class Maze:
    """Represents a 2D maze loaded from a text file."""

    grid: list[list[str]] = field(default_factory=list)
    start: tuple[int, int] | None = None
    goal: tuple[int, int] | None = None
    rows: int = 0
    cols: int = 0

    @classmethod
    def from_file(cls, filepath: str | Path) -> "Maze":
        """Load maze from a .txt file.

        Args:
            filepath: Path to the maze text file.

        Returns:
            Maze instance with grid, start and goal set.

        Raises:
            ValueError: If start or goal is missing, or maze is malformed.
            FileNotFoundError: If the file does not exist.
        """
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError(f"Maze file not found: {filepath}")

        grid: list[list[str]] = []
        start = None
        goal = None

        with path.open(encoding="utf-8") as f:
            for row_idx, line in enumerate(f):
                line = line.rstrip("\n")
                if not line:
                    continue
                row, row_start, row_goal = _parse_row(line, row_idx)
                if row_start:
                    start = row_start
                if row_goal:
                    goal = row_goal
                grid.append(row)

        _validate_grid(grid, start, goal)
        return cls(grid=grid, start=start, goal=goal, rows=len(grid), cols=len(grid[0]))

    def is_walkable(self, row: int, col: int) -> bool:
        """Return True if the cell is within bounds and not a wall."""
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False
        return self.grid[row][col] != WALL

    def display(self, path: list[tuple[int, int]] | None = None) -> str:
        """Return a string representation of the maze.

        Args:
            path: Optional list of (row, col) coordinates to mark with '*'.

        Returns:
            String with the maze, optionally with the solution path marked.
        """
        path_set = set(path) if path else set()
        lines = []
        for row_idx, row in enumerate(self.grid):
            rendered = []
            for col_idx, cell in enumerate(row):
                if (row_idx, col_idx) in path_set and cell == PATH:
                    rendered.append("*")
                else:
                    rendered.append(cell)
            lines.append("".join(rendered))
        return "\n".join(lines)