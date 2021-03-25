-- 나이순으로 오름차순 정렬
-- SELECT * FROM users
-- ORDER BY age ASC LIMIT 10;

-- 나이 + 성으로 오름차순 정렬 상위 10개
-- SELECT * FROM users
-- ORDER BY last_name, age ASC LIMIT 10; => ㄱㄴㄷ 정렬 기준에서 나이 어린 10명
-- ORDER BY age, last_name ASC LIMIT 10; => 나이가 어린 사람들 중에서 ㄱㄴㄷ정렬

-- 계좌잔액순으로 내림차순 정렬, 해당 사람의성, 이름
SELECT last_name, first_name, balance, age FROM users
ORDER BY balance DESC LIMIT 10;

-- 제일 부자 10명의 평균 나이
SELECT avg(age), avg(balance) FROM (SELECT * FROM users ORDER BY balance DESC LIMIT 10);