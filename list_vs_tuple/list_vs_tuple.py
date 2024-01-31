# Performance check between list and tuple
import sys
import timeit

# Checking the amount of time it takes to create a list vs a tuple
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))

# Checking the amount of space it takes to create a list vs a tuple
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

# Checking the amount of time it takes to iterate over a list vs a tuple
print(timeit.timeit(stmt="for _ in my_list: pass", globals=globals(), number=1000000))
print(timeit.timeit(stmt="for _ in my_tuple: pass", globals=globals(), number=1000000))

# Checking the amount of time it takes to access an element in a list vs a tuple    
print(timeit.timeit(stmt="my_list[0]", globals=globals(), number=1000000))
print(timeit.timeit(stmt="my_tuple[0]", globals=globals(), number=1000000))

# Checking the amount of time it takes to copy a list vs a tuple
print(timeit.timeit(stmt="my_list[:]", globals=globals(), number=1000000))
print(timeit.timeit(stmt="my_tuple[:]", globals=globals(), number=1000000))

