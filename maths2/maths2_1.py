# Координаты передаются через аргументы командной строки через пробел
import sys
import math
sum = 0
for el in sys.argv[1:]:
    sum += float(el)**2
l = math.sqrt(sum)
print("Length: " + str(l))
