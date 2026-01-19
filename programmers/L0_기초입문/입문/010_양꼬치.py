# 양꼬치
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 알고리즘: 기초
# 작성자: 김선영
# 작성일: 2026. 01. 19. 13:29:08

def solution(n, k):
    service = int(n // 10)
    lamb = 12000 * n
    coke = 2000 * (k - service)
    return lamb + coke