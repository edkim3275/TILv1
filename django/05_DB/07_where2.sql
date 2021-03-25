-- users에서 age 30 이상
-- SELECT first_name FROM users
-- where age >= 30;

-- users에서 성 = 김, 나이 >= 30의 성과 나이
SELECT age, last_name FROM users
WHERE age >= 30 AND last_name = '김';