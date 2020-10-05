### GROUP BY

1. 고양이와 개는 몇 마리 있을 까

   ```mysql
   SELECT ANIMAL_TYPE,COUNT(ANIMAL_TYPE) AS COUNT FROM ANIMAL_INS GROUP BY ANIMAL_TYPE
   ```

   

2. 동명 동물 수 찾기

   ```mysql
   SELECT NAME,COUNT(*) AS COUNT FROM ANIMAL_INS GROUP BY NAME 
   HAVING COUNT(NAME) >=2 AND NAME IS NOT NULL ORDER BY NAME
   ```

   

3. 입양 시작 구하기(1)

   ```mysql
   SELECT HOUR(DATETIME) AS HOUR, COUNT(HOUR(DATETIME)) AS COUNT 
   FROM ANIMAL_OUTS 
   WHERE 9<=HOUR(DATETIME) AND  HOUR(DATETIME)<=19
   GROUP BY HOUR(DATETIME) 
   ORDER BY HOUR(DATETIME)
   ```

   

4. 입양 시각구하기(2)

   ```mysql
   set @hour = -1;
   select
       (@hour := @hour +1) as HOUR,
       (select count(*) from animal_outs where hour(`datetime`) = @hour) as `COUNT`
   from animal_outs 
   where @hour < 23
   ```

   