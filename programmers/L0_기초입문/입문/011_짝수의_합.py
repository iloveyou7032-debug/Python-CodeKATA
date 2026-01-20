# 짝수의 합
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120831
# 알고리즘: 기초
# 작성자: 김선영
# 작성일: 2026. 01. 20. 13:50:33

def solution(n):
    even = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            even.append(i)
        else:
            continue
    return sum(even)
