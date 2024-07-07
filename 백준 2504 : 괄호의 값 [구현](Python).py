s = input()
stack = []
temp = 1
result = 0

for i in range(len(s)):
    # 열린 괄호들은 stack에 쌓고 temp 값 변경
    if s[i] == '(':
        temp *= 2
        stack.append('(')
    elif s[i] == '[':
        temp *= 3
        stack.append('[')
    # 닫힌 괄호들은 이전 괄호와 비교
    elif s[i] == ')':
        # stack이 비어있거나 직전 괄호 모양이 다르면
        if not stack or stack[-1] == '[':
            result = 0
            break
        # 쌍을 이루는 괄호일 경우
        elif s[i-1] == '(':
            result += temp
        # temp 초기화
        temp //= 2
        stack.pop()
    # 닫힌 괄호 ] 를 이전 괄호와 비교        
    else:
        # stack이 비어있거나 직전 괄호 모양이 다르면
        if not stack or stack[-1] == '(':
            result = 0
            break
        elif s[i-1] == '[':
            result += temp
        # temp 초기화
        temp //= 3
        stack.pop()

# stack이 비어있지 않은 경우    
if stack:
    result = 0
print(result)


### 결론

주어진 코드의 시간복잡도는 \( O(n) \)입니다. 이는 문자열의 길이에 선형적으로 비례합니다.
