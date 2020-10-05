### Sum,Max,Min



1. 최대값 구하기

   ```mysql
   # first
   SELECT DATETIME FROM ANIMAL_INS ORDER BY DATETIME DESC LIMIT 1;
   
   # second
   select max(datetime) as 시간 from animal_ins;
   ```

   

2. 최소값 구하기

   ```mysql
   SELECT DATETIME AS 시간 FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1;
   ```

   

3. 동물수 구하기

   ```mysql
   SELECT count(DATETIME) AS COUNT  FROM ANIMAL_INS
   ```

   

4. 중복제거하기

   ```mysql
   SELECT COUNT(DISTINCT(NAME)) AS COUNT FROM ANIMAL_INS
   ```

   

