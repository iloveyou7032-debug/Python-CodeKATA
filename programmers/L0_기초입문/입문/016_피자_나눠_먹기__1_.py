# 피자 나눠 먹기 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120814
# 알고리즘: 기초
# 작성자: 김선영
# 작성일: 2026. 01. 21. 11:39:37

def solution(n):
    if n % 7 == 0:
        return n // 7
    else:
        return n // 7 + 1