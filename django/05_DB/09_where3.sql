-- 값의 비교가 아닌 패턴의 비교 (LIKE)
-- SELECT * FROM users
-- -- WHERE age >= 20 and age < 30;
-- where age LIKE '2_';

-- 지역번호 02
-- SELECT phone, country FROM users
-- WHERE phone LIKE '02-%';

-- 준으로 끝나는 사람의 이름 가져오기
SELECT first_name FROM users
WHERE first_name LIKE '%준';

-- 박씨 이면서 준으로 끝나는 사람의 이름 가져오기
SELECT last_name, first_name FROM users
WHERE first_name LIKE '%준' and last_name LIKE '박'

-- 중간 번호가 5114인 사람
SELECT phone FROM users
WHERE phone LIKE '%-5114-%;