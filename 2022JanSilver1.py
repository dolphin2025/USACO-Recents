for tc in range(int(input())):
    a, b = [int(i) for i in input().split()]
    ans, minans = 0, 10**9
    while a > b:
        ans += a % 2 + 1
        a = int((a + 1) / 2)
    while b / 2 > a:
        ans += int(b) % 2 + 1
        b /= 2
    while a != int(b):
        minans = min(minans, ans + int(b) - a)
        ans += a % 2 + int(b) % 2 + 2
        a, b = int((a + 1) / 2), b / 2
    print(min(ans, minans))