import random
import time
import tracemalloc

import dane_z_pliku
from stos import Stos
from przeszukiwanie import Przeszukiwanie
from priorytetowy_stos import Priorytetowy_stos

amount, min, max = dane_z_pliku.pobierz_dane()

time1, time2, dif1, dif2, mem1, mem2 = 0, 0, 0, 0, 0, 0

tasks = []
tasks2 = []

for _ in range(amount):
    los = random.randint(min, max)
    tasks.append(los)
    tasks2.append(los)

start = time.time()
tracemalloc.start()
result = Przeszukiwanie(tasks).deep_search()
print(tracemalloc.get_traced_memory())
tracemalloc.stop()
time1 = time.time() - start

dif1 = abs(sum(result[0]) - sum(result[1]))

start = time.time()
tracemalloc.start()
result = Przeszukiwanie(tasks2).heuracy()
print(tracemalloc.get_traced_memory())
tracemalloc.stop()
time2 = time.time() - start

dif2 = abs(sum(result[0]) - sum(result[1]))

result_lenght = abs(len(result[0]) + len(result[1]))


print(f'całkowity czas testu deep search: {time1}')
print(f'całkowity czas testu heuracego: {time2}')
print(f'roznica miedzy procesami deep search: {dif1}')
print(f'roznica miedzy procesami heuracego: {dif2}')


'''get_traced_memory()
    Get the current size and peak size of memory blocks traced by tracemalloc.
    
    Returns a tuple: (current: int, peak: int).'''


