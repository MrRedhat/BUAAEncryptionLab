def get_inv(a, b):
    a_symbol = 1
    b_symbol = 1
    if a < 0:
        a_symbol = -1
    if b < 0:
        b_symbol = -1
    # 均按正数处理

    a0 = [a * a_symbol, 1, 0]
    b0 = [b * b_symbol, 0, 1]
    if a0[0] < b0[0]:
        a0, b0 = b0, a0
    while b0[0] > 0:
        k = a0[0] // b0[0]
        for i in range(0, 3):
            a0[i] = a0[i] - k * b0[i]
        a0, b0 = b0, a0
    answer = a0[1]
    while answer < 0:
        answer += b
    return answer * a_symbol * b_symbol
# 这是扩展欧几里得求逆元的函数


def crt(n, a, b):
    m = 1
    M = [1] * n
    x = 0
    for i in range(0, n):
        m *= a[i]
    for i in range(0, n):
        for j in range(0, n):
            if j == i:
                continue
            M[j] *= a[i]
    for i in range(0, n):
        x += M[i] * get_inv(M[i], a[i]) * b[i]
    x %= m
    if x == 0:
        x = m
    return x


def test():
    test = [[[23, 28, 33], [0, 0, 0]]]
    for i in range(0, 1):
        print(CRT(3, test[i][0], test[i][1]))


def main():
    astring = input()
    bstring = input()
    asp = astring.split(" ")
    bsp = bstring.split(" ")
    # 输入

    for i in range(0, n):
        asp[i] = int(asp[i])
        bsp[i] = int(bsp[i])

    print(CRT(3, asp, bsp))
    # 输出


if __name__ == '__main__':
    test()


