import math
import datetime as dt
import my_module as m
from packet import integers as i, strings as s

            #Задание 1
def now():
    print(dt.datetime.now())

def cor(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        print("Нельзя извлечь корень")

print(cor(4))
now()
print("-------------")
            # Задание 2
print(m.sum_func(4, 8))
print("---------------------")
            # Задание 3

print(i.mult(4, 8), i.fact(5))
st = "Эта строка состоит из символов"
c = s.chars_counter(st) + len(str(s.chars_counter(st)))
print(s.splitter("dsds dsada dsadad sdadas dsada dsada", " "), " " + f"Эта строка состоит из  {c} символов")