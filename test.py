import sys

my_list = []
for line in sys.stdin:
    if int(line) == 0:
        break
    my_list.append(int(line))
count = 1
my_max = -1
for el in my_list:
    if el > my_max:
        my_max = el
        count = 1
    elif el == my_max:
        count += 1
print(count)