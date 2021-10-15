my_set = {1, 2, 3, 4}

my_input = int(input())

temp_set = set()

temp_set.add(my_input)

my_set.update(temp_set)

print(my_set)
