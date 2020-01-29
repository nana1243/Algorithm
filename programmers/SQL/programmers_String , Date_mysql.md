## String , Date

1. 루시와 엘라 찾기

   ```mysql
   SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE FROM ANIMAL_INS 
   WHERE NAME IN( "Lucy" , "Ella" ,"Pickle" ,"Rogan" ,"Sabrina" ,"Mitty")
   ```

   

2. 이름에 el이 들어가는 동물찾기

   ```mysql
   SELECT ANIMAL_ID,NAME FROM ANIMAL_INS
   WHERE (NAME LIKE "%EL%") and  (ANIMAL_TYPE="Dog")
   ORDER BY NAME
   ```

   

3. 중성화 여부 파악하기

   ```mysql
   SELECT ANIMAL_ID, NAME, 
   CASE WHEN SEX_UPON_INTAKE LIKE "%Neutered%" OR SEX_UPON_INTAKE LIKE "%Spayed%" 
   THEN "O"
   ELSE 'X' END AS "중성화" 
   FROM ANIMAL_INS
   ORDER BY ANIMAL_ID
   ```

   

4. 오랜 기간 보호한 동물(2)

   ```mysql
   SELECT INS.ANIMAL_ID, INS.NAME 
   FROM ANIMAL_INS AS INS
   INNER JOIN ANIMAL_OUTS AS OUTS
   ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
   ORDER BY OUTS.DATETIME - INS.DATETIME DESC
   LIMIT 2
   ```

   

5. DATETIME에서 DATE로 형변환

   ```mysql
   SELECT ANIMAL_ID, NAME,  cast (datetime as date) AS 날짜 
   FROM ANIMAL_INS
   ORDER BY ANIMAL_ID
   ```

   

   