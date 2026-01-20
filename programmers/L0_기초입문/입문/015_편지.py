# 편지
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120898
# 알고리즘: 기초
# 작성자: 김선영
# 작성일: 2026. 01. 20. 14:04:06

def solution(message):
    a_list = []
    for i in message:
        a_list.append(i)
    answer = len(a_list) * 2
    return answer