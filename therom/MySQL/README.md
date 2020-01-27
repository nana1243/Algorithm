1. MYSQL 기본내용

   > **기본 구조**
   >
   > SELECT [DISTINCT] 컬럼, 그룹 함수(컬럼)
   >
   > FROM 테이블명
   >
   > [WHERE 조건]
   >
   > [GROUP BY Group대상]
   >
   > [HAVING 그룹 함수 포함 조건]
   >
   > [ORDER BY 정렬대상 [ASC/DESC]]
   >
   > [LIMIT N]

   

   1-1 아래에서 담겨질 내용

   > #### 1. 역순으로 나열하기 - DESC
   >
   > #### 2. 두가지 요소로 나열하기 - ORDER BY 1번째 요소 DESC , 2번째 요소 ASC
   >
   > #### 3. 상위 N개 뽑아내기 - LIMIT N
   >
   > #### 4. 최대 최소, 평균, Count 함수 쓰기 - MIN(*column_name*), MAX(*column_name*), AVG(*column_name*)
   >
   > #### 5. 중복제거하기 - count( *column_name*) vs  count(DINTINCT(*column_name*))
   >
   > #### 6. 동명이인찾기 - GROUP BY NAME HAVING COUNT(NAME) >=2
   >
   > #### 7. 시간함수 다루기 -  최초시간, 가장빠른시간 ...등등
   >
   > #### 8. WHERE조건절 OR

   

   

   2.역순으로 나열하기

   ```mysql
   # 역순으로 나열하기
   
   SELECT NAME, DATETIME FROM ANIMAL_INS ORDER BY ANIMAL_ID DESC
   
   
   ```

   

2. 두가지 요소 고려하기 

   - 첫번째 요소 : 이름
   - 두번째 요소 : 만약에 이름이 같다면 DATETIME 역순으로 고려

   ```mysql
   SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS ORDER BY NAME ASC ,DATETIME DESC
   ```

3. 상위 N개 뽑아내기

   - 가장 먼저 N개 뽑아내기 = limit 과 order by를 고려해야한다

   ```MYSQL
   SELECT NAME  FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1;
   ```

4. 최대 최소값 구하기 : MIN(DATETIME) -가장 오래된 시간 , MAX(DATETIME) - 가장 최신 순서

   ```mysql
   -- order를 활용해
   SELECT DATETIME as 시간 FROM ANIMAL_INS ORDER BY DATETIME DESC LIMIT 1;
   
   -- max를 활용하여
   select max(datetime) as 시간 from animal_ins;
   
   ```

5. 등록 수 구하기

   - NULL 값의 유/무 확인해줘야 할때

   ```mysql
   SELECT count(DATETIME) AS COUNT  FROM ANIMAL_INS
   ```

6. 중복제거하기 :DISCTINCT 함수 쓰기

   ```mysql
   SELECT COUNT(DISTINCT(NAME)) AS COUNT FROM ANIMAL_INS
   ```

7. GROUP BY 를 통해

   ```MYSQL
   SELECT ANIMAL_TYPE,COUNT(ANIMAL_TYPE) AS COUNT FROM ANIMAL_INS GROUP BY ANIMAL_TYPE
   ```

   

9.동명이인 찾기 + HAVING절 쓰기 



```mysql
SELECT NAME,COUNT(*) AS COUNT FROM ANIMAL_INS GROUP BY NAME 
HAVING COUNT(NAME) >=2 AND NAME IS NOT NULL ORDER BY NAME
```

#### HAVING 절에 대한 소개

>HAVING 절은 해석상 WHERE 절과 동일하다. 단 조건 내용에 그룹 함수를 포함하는 것만을 포함한다.
>
>일반 조건은 WHERE 절에 기술하지만 그룹 함수를 포함한 조건은 HAVING 절에 기술한다.
>
>**기본 구조**
>
>SELECT [DISTINCT] 컬럼, 그룹 함수(컬럼)
>
>FROM 테이블명
>
>[WHERE 조건]
>
>[GROUP BY Group대상]
>
>[HAVING 그룹 함수 포함 조건]
>
>[ORDER BY 정렬대상 [ASC/DESC]]
>
>

10. 시간함수 사용하기

    - DATETIME : 시간으로 정렬하기

    ```mysql
    SELECT HOUR(DATETIME) AS HOUR, COUNT(HOUR(DATETIME)) AS COUNT 
    FROM ANIMAL_OUTS 
    WHERE 9<=HOUR(DATETIME) AND  HOUR(DATETIME)<=19
    GROUP BY HOUR(DATETIME) 
    ORDER BY HOUR(DATETIME)  
    ```

    CF> 여기서 BETWEEN 을 써서 해결 할 수 있다(WHERE절)





11. WHERE조건절 중 AND와 OR

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



> 앞에 OR 을 쓸때 조건까지 다 써주자! (틀렷던 기억!)

