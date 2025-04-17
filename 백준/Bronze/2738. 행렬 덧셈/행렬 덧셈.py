A, B = [], []

# N: 행의 수, M: 열의 수
N, M = map(int, input().split())

# 행렬 A 입력
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

# 행렬 B 입력
for _ in range(N):
    row = list(map(int, input().split()))
    B.append(row)

# A와 B의 각 원소를 더한 후 출력
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print()  # 줄 바꿈
