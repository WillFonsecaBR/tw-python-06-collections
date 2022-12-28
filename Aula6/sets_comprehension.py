# UTILIZANDO SET COMPREHENSION
set_01 = {1, 23, 3, 50}
set_02 = set([1, 2, 3, 4, 20, 18, 25, 5, 9])

set_comprehension = {i * i for i in range(0, 10)}
print(f"set_comprehension = {set_comprehension}")

set_comprehension_2 = {i for i in set_01.union(set_02)}
print(f"set_comprehension_2 = {set_comprehension_2}")
