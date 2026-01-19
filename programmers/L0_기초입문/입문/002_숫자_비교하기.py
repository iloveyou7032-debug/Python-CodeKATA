# 숫자 비교하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120807
# 알고리즘: 기초
# 작성자: 김선영
# 작성일: 2026. 01. 19. 11:02:41

def solution(num1, num2):
    def check(x, lower, upper):
        return lower <= x <= upper
    
    conform1 = check(num1, 0, 10000)
    conform2 = check(num2, 0, 10000)
    
    assert conform1 and conform2
    
    if num1 == num2:
        return 1
    else:
        return -1