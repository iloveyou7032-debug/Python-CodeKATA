# 즐겨찾기가 가장 많은 식당 정보 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131123
# 작성자: 김선영
# 작성일: 2026. 01. 19. 10:22:08

-- from 서브퀴리
select 
    faver_rnk.FOOD_TYPE
    , faver_rnk.REST_ID
    , faver_rnk.REST_NAME
    , faver_rnk.FAVORITES
from (
    select
        FOOD_TYPE
        , REST_ID
        , REST_NAME
        , FAVORITES
        , rank() over(partition by FOOD_TYPE order by FAVORITES desc) as rnk
    from REST_INFO
    ) as faver_rnk
where faver_rnk.rnk = 1
order by faver_rnk.FOOD_TYPE desc