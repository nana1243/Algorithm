### JOIN



1. 없어진 기록 찾기

   ```mysql
   SELECT OUTS.ANIMAL_ID , OUTS.NAME
   FROM ANIMAL_OUTS as OUTS
   LEFT OUTER JOIN ANIMAL_INS AS INS
   ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
   WHERE INS.ANIMAL_ID IS NULL
   ORDER BY OUTS.ANIMAL_ID
   ```

   

2. 있었는데요 없었습니다

   ```mysql
   SELECT INS.ANIMAL_ID, INS.NAME
   FROM ANIMAL_INS AS INS
   LEFT OUTER JOIN ANIMAL_OUTS AS OUTS
   ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
   WHERE INS.DATETIME >= OUTS.DATETIME
   ORDER BY INS.DATETIME
   ```

   

3. 오랜 기간 보호한 동물(1)

   ```mysql
   SELECT INS.NAME, INS.DATETIME
   FROM ANIMAL_INS AS INS
   LEFT OUTER JOIN ANIMAL_OUTS AS OUTS
   ON INS.ANIMAL_ID  = OUTS.ANIMAL_ID
   WHERE OUTS.ANIMAL_ID IS NULL
   ORDER BY INS.DATETIME 
   LIMIT 3;
   ```

   

4. 보호소에서 중성화한 동물

   ```mysql
   SELECT 
   OUTS.ANIMAL_ID, OUTS.ANIMAL_TYPE, OUTS.NAME
   FROM ANIMAL_INS AS INS 
   INNER JOIN ANIMAL_OUTS AS OUTS
   ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
   where (INS.SEX_UPON_INTAKE LIKE "%Intact%") 
   AND 
   (OUTS.SEX_UPON_OUTCOME LIKE "%Neutered%" OR 
    OUTS.SEX_UPON_OUTCOME LIKE "%Spayed%" )
   ORDER BY OUTS.ANIMAL_ID
   ```

   