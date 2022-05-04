March 21, 2021
# Algorytmy i struktury danych
## 1 Implementacja algorytmów sortowania

Napisz cztery funkcje sortujące, które implementują następujące algorytmy:
- sortowanie bąbelkowe (ang.bubble sort),
- sortowanie przez wybieranie (ang.selection sort),
- sortowanie przez scalanie (ang.merge sort),
- sortowanie szybkie (ang.quick sort).

Każda z funkcji powinna przyjmować jako argument listę i zwracać listę posortowaną, np.:

```
>>> bubble_sort([3,5,1])
[1,3,5]
```

## 2  Porównanie algorytmów sortowania

Jako dane do sortowania wykorzystaj plikpan-tadeusz.txt, zawierający słowa oddzielone białymi znakami. Dla każdej z funkcji sortujących:
- sprawdź czy funkcja poprawnie sortuje słowa wczytywane z pliku,
- zmierz czas sortowania list zawierających `n` pierwszych słów wczytanych zpliku (np.n= 1000, 2000, . . . , 10000),
- wygeneruj wykres zależności czasu sortowania od długości listy.

Zwróć uwagę by mierzyć wyłącznie czas sortowania, pomijając wczytywaniedanych lub wyświetlanie wyników.  Do pomiaru czasu można użyć funkcji `timeit`(import timit):
```
>>> timeit.timeit("sorted([1,3,5])", number=100000)
0.06795001029968262
```

która zwraca czas (w sekundach) wykonania podanego wyrażenia (w tym przypadku `sorted([1,3,5]`)) określoną liczbę razy (w tym przypadku 100000).Przy korzystaniu z funkcji timeit należy zadbać by w trakcie pomiarów niewykonywały się inne procesy mocno obciążające procesor. 

Do tworzenia wykresów można użyć biblioteki `Matplotlib`(https://matplotlib.org). Biblioteka ta oferuje dwa zestawy funkcji (API): object-oriented i py-plot, z których ten drugi daje mniejsze możliwości, ale jest prostszy w użyciu. Aby utworzyć plik PNG z wykresem, należy zamiast funkcji show() użyć savefig('plik.png').

## 3  Wyniki
Rezultatem powinny być:
- kod źródłowy z zaimplementowanymi funkcjami sortującymi,
- kod źródłowy przeprowadzający komplet pomiarów wydajności i generujący pliki PNG z wykresami,
- wygenerowane pliki PNG z wykresami.
