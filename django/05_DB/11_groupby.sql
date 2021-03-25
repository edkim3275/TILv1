-- 각 성씨가 몇 명이 있을까?
-- SELECT DISTINCT last_name FROM users; -- 발견한 순서대로


SELECT last_name, COUNT(*) AS name_count
FROM users
GROUP BY last_name; -- last_name이 같은 사람들만 따로 SELECT 구분 진행
