# Generator comprehension and memory saving
import sys

sqrd_num_lc = [x**2 for x in range(1000000)]
sqrd_num_gc = (x**2 for x in range(1000000))

print(sys.getsizeof(sqrd_num_lc))
print(sys.getsizeof(sqrd_num_gc))
