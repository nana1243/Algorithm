# case , date함수 다루기 , set



### 1. CASE문

```mysql
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    WHEN conditionN THEN resultN
    ELSE result
END;
```



EX>  조건을 통해 칼럼을 만들고 그것을 추출 하려할때

```mysql
SELECT COLUMN1, COLUMN2, 

CASE 

WHEN + 조건1 + THEN 결과 1

WHEN + 조건2 + THEN 결과 2

ELSE  + 결과 3

END AS (CASE를 통해 새로운 COLUMN2)

FROM TABLE명
```



### 2. DATE함수 연산

> - DATE - format YYYY-MM-DD
> - DATETIME - format: YYYY-MM-DD HH:MI:SS
> - TIMESTAMP - format: YYYY-MM-DD HH:MI:SS
> - YEAR - format YYYY or YY

#### 2-1 DATE_FORMAT()함수

```mysql
 date_format(datetime, '%Y-%m-%d') 
```



- 아래처럼 위에서 뽑은 내용을 더 협소하게 뽑아내고 싶을때

```mysql
date_format(datetime, '%m') 
```



```mysql
select cast(datetime as date) from animal_outs
```

![cast(datetime,date)](https://user-images.githubusercontent.com/52269210/73164358-2818af80-4135-11ea-9e7b-cf428be9de3e.JPG)



```mysql
select cast(datetime as time) from animal_outs
```

![cast(datetime,time)](https://user-images.githubusercontent.com/52269210/73164359-2818af80-4135-11ea-9725-7cf60ba8ff7b.JPG)

```mysql
select hour(datetime) from animal_outs

-- 아래와 같은 형태로 쓸 수 있다 --
select year(datetime) from animal_outs
select month(datetime) from animal_outs
select day(datetime) from animal_outs
```

![hour(time)](https://user-images.githubusercontent.com/52269210/73164361-28b14600-4135-11ea-9ac9-fb32c48c98a7.JPG)



위 사진은 hour(datetime)

% 시간대별로 집계하는 함수 + set을 이용%



```mysql
set @hour = -1;
select
    (@hour := @hour +1) as HOUR,
    (select count(*) from animal_outs where hour(`datetime`) = @hour) as `COUNT`
from animal_outs 
where @hour < 23
```

