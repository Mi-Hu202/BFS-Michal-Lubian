# Raport z eksperymentu – BFS Maze Solver

## 1. Opis przeprowadzonych testów

Testy podzielono na dwie kategorie:

**Testy jednostkowe** (`tests/`) – weryfikują poprawność działania kodu:

- Wczytywanie labiryntu z pliku (poprawny plik, brak startu, brak mety, nieistniejący plik)
- Sprawdzanie przechodniości komórek (`is_walkable`)
- Renderowanie labiryntu z zaznaczoną ścieżką
- Znajdowanie ścieżki w prostych przypadkach
- Obsługa labiryntu bez rozwiązania (`None`)
- Poruszanie się algorytmu wokół ścian
- Duży labirynt z pętlami

**Testy funkcjonalne** (ręczne) – uruchomienie solvera na 3 przykładowych labiryntach:

| Plik | Rozmiar | Rozwiązanie |
|------|---------|-------------|
| `maze_simple.txt` | 6×8 | Tak |
| `maze_medium.txt` | 13×14 | Tak |
| `maze_no_solution.txt` | 3×3 | Brak |

## 2. Uzyskane wyniki

### maze_simple.txt

```
Maze loaded: 6 rows × 8 cols
Start: (0, 0)  |  Goal: (5, 7)
Path found! Length: 14 steps  |  Time: ~0.04 ms
```

### maze_medium.txt

```
Maze loaded: 13 rows × 14 cols
Start: (0, 0)  |  Goal: (12, 12)
Path found! Length: 31 steps  |  Time: ~0.12 ms
```

### maze_no_solution.txt

```
Maze loaded: 3 rows × 3 cols
Start: (0, 0)  |  Goal: (2, 2)
No path found – the maze has no solution.
```

Wszystkie testy jednostkowe przeszły pomyślnie (`pytest`).

## 3. Wnioski

- Algorytm BFS poprawnie znajduje **najkrótszą ścieżkę** w każdym testowalnym przypadku.
- Czas działania jest pomijalnie mały dla labiryntów testowych (poniżej 1 ms), co potwierdza
  liniową złożoność O(V+E) w stosunku do rozmiaru siatki.
- Algorytm poprawnie zwraca `None` dla labiryntów bez rozwiązania, zamiast zawieszać się
  lub generować wyjątek.
- BFS jest optymalny dla grafów nieważonych (każdy krok = koszt 1). Dla labiryntów z
  różnymi kosztami przejścia lepszym wyborem byłby algorytm Dijkstry lub A*.
- Implementacja jest czytelna, modularna i w pełni pokryta testami jednostkowymi.
