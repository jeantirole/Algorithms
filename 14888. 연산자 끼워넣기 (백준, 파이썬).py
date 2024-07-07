def dfs(n, sm, add, sub, mul, div):
    global mn, mx
    # [0] 결과값/중간 값의 범위: int(-1e8)~int(1e8)
    if sm < int(-1e9) or int(1e9)<sm:
        return

    # [1] 종료조건(정답처리)
    if n==N:
        mn = min(mn, sm)
        mx = max(mx, sm)
        return

    # [2] 하부호출: 연산자 개수 남았을 경우만 호출 가능
    if add>0:
        dfs(n+1, sm+lst[n], add-1, sub, mul, div)
    if sub>0:
        dfs(n+1, sm-lst[n], add, sub-1, mul, div)
    if mul>0:
        dfs(n+1, sm*lst[n], add, sub, mul-1, div)
    if div>0:
        dfs(n+1, int(sm/lst[n]), add, sub, mul, div-1)

N = int(input())
lst = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

mn, mx = int(1e9), int(-1e9)
dfs(1, lst[0], add, sub, mul, div)
print(mx, mn, sep='\n')

# 시간복잡도
최악의 경우, 모든 연산자를 사용할 수 있다고 가정하면 각 단계마다 4개의 호출이 이루어지므로 시간복잡도는 다음과 같이 계산할 수 있습니다.
\[ T(N) = 4^{(N-1)} \]
즉, 시간복잡도는 \( O(4^N) \) 입니다.
