# 첫 줄 입력: N과 X
N, X = map(int, input().split())

# 두 번째 줄 입력: 수열 A
A = list(map(int, input().split()))

# 결과를 저장할 리스트
result = []

# A의 원소 중 X보다 작은 것만 result에 추가
for num in A:
    if num < X:
        result.append(str(num))

# 결과 출력
print(" ".join(result))
