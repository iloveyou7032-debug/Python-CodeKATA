# 오랜 기간 보호한 동물(1)
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59044
# 작성자: 김선영
# 작성일: 2026. 01. 19. 09:32:14

select 
    ai.NAME
    , ai.DATETIME
from ANIMAL_INS ai
    left join ANIMAL_OUTS ao
    on ai.ANIMAL_ID = ao.ANIMAL_ID
where ao.animal_id is null
order by ai.DATETIME
limit 3