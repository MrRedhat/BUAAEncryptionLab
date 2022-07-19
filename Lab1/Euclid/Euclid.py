def exgcd(a, b):
    x_symbol = 1
    y_symbol = 1
    if a < 0:
        a = -a
        x_symbol = -1
    if b < 0:
        b = -b
        y_symbol = -1
    # 均按正数处理

    if b == 0:
        return 1, 0, a
    else:
        x, y, g = exgcd(b, a % b)
        x, y = y, (x - (a // b) * y)

        # 最小正整数x
        while x <= 0:
            x += b // g
            y -= a // g

        return x * x_symbol, y * y_symbol, g


def test():
    test = [[7, 5], [31, -13], [33329114838577399, 940427085844835513],
            [319947760790973750446679509618867702761, 224671033548424530946344620390486244671]]
    for i in range(0, len(test)):
        print(exgcd(test[i][0], test[i][1]))


def main():
    sin = input()
    a, b = sin.split(" ")
    a = int(a)
    b = int(b)
    # 输入

    x, y, g = exgcd(a, b)
    # 计算

    print(x, end=' ')
    print(y, end=' ')
    print(g)
    # 输出

if __name__ == '__main__':
    test()
