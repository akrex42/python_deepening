import sys

digit_string = sys.argv[1]
count = 0
for i in range(0, len(digit_string)):
    count += int(digit_string[i])
print(count)

# tutors' solution
# import sys
# print(sum([int(x) for x in sys.argv[1]]))
