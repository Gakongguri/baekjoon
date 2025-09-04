L = int(input())
S = input().strip()

M = 1234567891
r = 31
result = 0
power = 1  # r^0

for c in S:
    val = ord(c) - ord('a') + 1
    result = (result + val * power) % M
    power = (power * r) % M

print(result)
