import random
import time
chromosomu = [67, 52, 42, 69, 14, 88, 1488, 'сука їбана']
collegu = ['Maksym', 'Marko', "NaZar", "Yarema", 'Yulian']

while True:
    w = random.choice(chromosomu)
    n = random.choice(collegu)
    m = f"Дирявий хуєсос - {n}, кількість хромосом - {w}"
    time.sleep(1)
    print(m)
