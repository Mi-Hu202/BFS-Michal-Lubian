# BFS Maze Solver

[![python](https://img.shields.io/badge/Python-3.14-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

Projekt zaliczeniowy z przedmiotu **Sztuczna Inteligencja** (Stacjonarne 2025/26).

Implementacja algorytmu **BFS (Breadth-First Search)** do znajdowania najkrótszej drogi
w labiryncie opisanym w pliku tekstowym.

---

## Opis problemu

Labirynt reprezentowany jest jako siatka znaków w pliku `.txt`:

| Znak | Znaczenie |
|------|-----------|
| `S`  | Punkt startowy |
| `G`  | Cel (meta) |
| `#`  | Ściana (nieprzejezdna) |
| `.`  | Wolna droga |

Celem jest znalezienie **najkrótszej** ścieżki od `S` do `G`.

## Algorytm BFS

BFS (Breadth-First Search) przeszukuje graf **poziomami** — najpierw wszystkie sąsiednie
komórki odległe o 1 krok, potem o 2 kroki, itd. Dzięki temu **pierwsza znaleziona ścieżka
jest zawsze najkrótsza** (minimalna liczba kroków).

Złożoność czasowa i pamięciowa: **O(V + E)**, gdzie V = liczba komórek, E = liczba
sąsiedztw (krawędzi grafu).

## Wymagania

- Python ≥ 3.14
- [uv](https://github.com/astral-sh/uv) (menedżer środowiska)

## Instalacja i uruchomienie

```bash
# 1. Sklonuj repozytorium
git clone https://github.com/YOUR_USERNAME/bfs-maze.git
cd bfs-maze

# 2. Zainstaluj zależności deweloperskie przez uv
uv sync --group dev

# 3. Uruchom solver na przykładowym labiryncie
uv run maze-solver data/maze_simple.txt

# 4. Lub bezpośrednio przez Python
uv run python -m app.main data/maze_medium.txt
```

## Oczekiwany wynik

Po uruchomieniu `uv run maze-solver data/maze_simple.txt` program wypisuje na standardowe wyjście:

```
Maze loaded: 7 rows × 7 cols
Start: (0, 0)  |  Goal: (6, 6)

Path found! Length: 12 steps  |  Time: 0.051 ms

S......
*#####.
*#...#.
*#.#.#.
*#...#.
*#####.
******G

Path coordinates:
(0, 0) -> (1, 0) -> (2, 0) -> (3, 0) -> (4, 0) -> (5, 0) -> (6, 0) -> (6, 1) -> (6, 2) -> (6, 3) -> (6, 4) -> (6, 5) -> (6, 6)
```

Gwiazdki (`*`) oznaczają znalezioną najkrótszą ścieżkę. Dla labiryntu bez rozwiązania (`maze_no_solution.txt`) program wypisze:

```
Maze loaded: 3 rows × 3 cols
Start: (0, 0)  |  Goal: (2, 2)

No path found – the maze has no solution.
```

Aby ukryć wizualizację i wypisać tylko statystyki:

```bash
uv run maze-solver data/maze_simple.txt --hide-path
```

## Uruchamianie testów

```bash
uv run pytest
```

## Przykładowy wynik

```
Maze loaded: 6 rows × 8 cols
Start: (0, 0)  |  Goal: (5, 7)

Path found! Length: 14 steps  |  Time: 0.042 ms

S**#...
.###*##.
.....*#.
#.###**.
#.#...**
..#.##.G

Path coordinates:
(0, 0) -> (0, 1) -> (0, 2) -> ...-> (5, 7)
```

## Struktura projektu

```
bfs-maze/
├── app/
│   ├── __init__.py
│   ├── bfs.py       # Implementacja algorytmu BFS
│   ├── maze.py      # Klasa Maze – wczytywanie i reprezentacja labiryntu
│   └── main.py      # Punkt wejścia (CLI)
├── tests/
│   ├── test_bfs.py  # Testy jednostkowe BFS
│   └── test_maze.py # Testy jednostkowe Maze
├── data/
│   ├── maze_simple.txt      # Mały labirynt przykładowy
│   ├── maze_medium.txt      # Większy labirynt
│   └── maze_no_solution.txt # Labirynt bez rozwiązania
├── REPORT.md
├── pyproject.toml
└── README.md
```

---

Copyright (c) 2026 — Projekt zaliczeniowy AI
