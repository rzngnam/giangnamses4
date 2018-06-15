while True:
    n = int(input("Size ( odd , > 1 ) :  "))
    if (n % 2 == 0) or (n < 2):
        print('nhập lỗi')
        break
    for i in range(4):
        if i == 2:
            for j in range(n - 1):
                print('* ', end='')
            print('   ', end='')
            continue
        for j in range(n):
            print('* ', end='')
        print('   ', end='')
    print()
    for i in range(n-2):
        if i == (n // 2)-1:
            for j in range(n*10):
                if (j == 0) or (j == n * 2 + 3) or (j == n * 4 + 1) or (j == n * 4 + 6) \
                        or (j == n*6 + 4) or (j == n*6 + 7):
                    print('*', end='')
                elif j in range(n * 6 + 9, n*7 + 8):
                    print('* ', end='')
                else:
                    print(' ', end='')
        else:
            for j in range(n*10):
                if (j == 0) or (j == n*2 + 3) or (j == n*4 + 1) or (j == n*4 + 6) \
                        or (j == n*6 + 4) or (j == n*6 + 7):
                    print('*', end='')
                else:
                    print(' ', end='')
        print()
    for i in range(4):
        if i == 2:
            for j in range(n - 1):
                print('* ', end='')
            print('   ', end='')
            continue
        for j in range(n):
            print('* ', end='')
        print('   ', end='')
    print()
