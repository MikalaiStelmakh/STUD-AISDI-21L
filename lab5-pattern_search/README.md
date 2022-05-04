May 6, 2021
# Algorytmy i struktury danych - Wyszukiwanie wzorca w tekście

## 1  Implementacja algorytmów wyszukiwania wzorca
Napisz trzy funkcje, które implementują następujące algorytmy wyszukiwania wzorca w tekście:
- algorytm N (tzw. naiwny) — `find_n`,
- algorytm KMP (Knutha-Morrisa-Pratta) — `find_kmp`,
- algorytm KR (Karpa-Rabina) — `find_kr`

Implementacja powinna używać nazw funkcji podanych powyżej, wszystkie funkcje powinny mieć identyczny interfejs w postaci:
```python
def find(substring: str, text: str) -> List[int]:
"""
Parameters:
    substring: substring to be found
    text: text to be searched
Returns:
    List of positions in ascending order of the beginnings
    of``substring``in``text``.
"""
```
## 2  Sprawdzenie poprawności implementacji
Przetestuj wszystkie funkcje dla przypadków brzegowych:
- pusty jeden lub oba napisy wejściowe,
- napis `substring` równy napisowi `text`,
- napis `substring` dłuższy od napisu `text`,
- napis `substring` nie występuje w `text`.

Przetestuj implementację algorytmu naiwnego (dobierz kilka zestawów danych testowych oraz sprawdź poprawność wyników). Następnie przetestuj implementację pozostałych algorytmów w ten sposób, że dla generowanych losowo tekstów i wzorców (alfabet ogranicz do dwóch liter), sprawdź czy wszystkie implementacje zwracają ten sam wynik.

## 3  Porównanie algorytmów wyszukiwania wzorca
Jako tekst przeszukiwany wykorzystaj plik *pan-tadeusz.txt*. Dla każdej z funkcji:
- zmierz czas wyszukiwania w całym pliku `n` pierwszych słów wczytanych z pliku (np.n= 100, 200,. . . , 1000).

Narysuj zbiorczy wykres ( jeden wykres dla trzech funkcji) pokazujący zależność czasu wyszukiwania od liczby szukanych słów.

## 4  Wyniki
Rezultatem powinny być:
- kod źródłowy z zaimplementowanymi funkcjami,
- kod źródłowy przeprowadzający komplet testów (punkt 2) i wyświetlający wyniki testów na ekranie,
- zrzut ekranu z wyświetlonymi wynikami testów,
- kod źródłowy przeprowadzający komplet pomiarów wydajności (punkt 3) i generujący plik zwykresem,
- wygenerowany plik z wykresem.
