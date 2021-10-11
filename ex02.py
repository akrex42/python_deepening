import sys

size = int(sys.argv[1])

for i in range(1, size + 1):
    for j in range(1, size + 1 - i):
        print(' ', end='')
    for k in range(0, i):
        print('#', end='')
    print()
    
# tutors solution
# import sys
#
# num_steps = int(sys.argv[1])
#
# for i in range(num_steps):
#     print(" " * (num_steps - i - 1), "#" * (i + 1), sep="")
