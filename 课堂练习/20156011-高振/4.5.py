def get_one(n):
    list = []
    for i in range(1, n):
        list.append(2 ** i - 1)
    return list


def main():
    x = int(input())
    list = get_one(x)
    print(list)
    print(1)
    for i in range(1, x):
        fg = 0
        for j in range(2, i - 1):
            if list[i] % j == 0:
                fg = 1
                break
        if fg == 0:
            print(list[i])


if __name__ == '__main__':
    main()
