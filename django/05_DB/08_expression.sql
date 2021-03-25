-- users 레코드의 개수
-- SELECT COUNT(*) FROM users;

SELECT COUNT(*) FROM users
where age >= 30;


-- 30살 이상의 평균 나이
-- SELECT AVG(age) FROM users
-- WHERE age >= 30;

-- 계좌잔액이 가장 높은 사람의 액수는?
-- SELECT first_name, max(balance) FROM users;

-- 전체 계좌 잔액
-- SELECT sum(balance), first_name FROM users;