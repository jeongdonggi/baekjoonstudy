-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS AS I LEFT JOIN ANIMAL_OUTS AS O USING(ANIMAL_ID, NAME, ANIMAL_TYPE)
ORDER BY O.DATETIME - I.DATETIME DESC
LIMIT 2