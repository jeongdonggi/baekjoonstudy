-- 코드를 작성해주세요
SELECT ITEM_ID, ITEM_NAME
FROM ITEM_INFO I INNER JOIN ITEM_TREE T USING(ITEM_ID)
WHERE T.PARENT_ITEM_ID IS NULL