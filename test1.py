def find_closest(size, amount, my_list):
    centre = size / 2
    i = 1
    for item in my_list:
        if item <= centre < item + 1:
            print(item)
        elif item <= centre < my_list[i]:
            print(item, my_list[i])
        i += 1


if __name__ == "__main__":
    size, amount = map(int, input().split())
    my_list = list(map(int, input().split()))

    find_closest(size, amount, my_list)
