# 조건에 맞는 사용자와 총 거래금액 조회하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/164668
# 작성자: 김선영
# 작성일: 2026. 01. 19. 09:55:40

select 
    u.USER_ID
    , u.NICKNAME
    , sum(PRICE) as TOTAL_SALES
from USED_GOODS_BOARD b
    join USED_GOODS_USER u
    on b.WRITER_ID = u.USER_ID
where b.STATUS = "DONE"
group by u.USER_ID, u.NICKNAME
having sum(PRICE) >= 700000
order by TOTAL_SALES;