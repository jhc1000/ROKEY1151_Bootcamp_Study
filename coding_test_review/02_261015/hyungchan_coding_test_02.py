

from collections import deque

def solution(A, B):
    answer = 0
    dq1 = deque(list(A))
    for i in range(len(list(A))):
        # print(list(dq1))
        if list(dq1) != list(B):
            dq1.rotate()
            answer += 1
        else:
            return answer
    return -1

print(solution("hello", "ohell"))
print(solution("apple", "elppa"))
print(solution("atat", "tata"))
print(solution("abc", "abc"))


print('---------')

# 솔루션
solution=lambda a,b:(b*2).find(a)

print(solution("hello", "ohell"))
print(solution("apple", "elppa"))
print(solution("atat", "tata"))
print(solution("abc", "abc"))

print("ohellohell".find("hello"))

"""
(method) def find(
    sub: str,
    start: SupportsIndex | None = None,
    end: SupportsIndex | None = None,
    /
) -> int
Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].

Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.
"""