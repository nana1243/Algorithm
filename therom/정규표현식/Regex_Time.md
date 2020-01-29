## python dates [시간 정규 함수식]

[출처 : w3school 에서 배운 내용을 제 나름대로 적어놨습니다]

### 2.The strftime() Method

The `datetime` object has a method for formatting date objects into readable strings.

The method is called `strftime()`, and takes one parameter, `format`, to specify the format of the returned string:

> 생성된 datetime을 좀더 읽을 수 있게 변할 수 있게 하는 methods가 strftime()이다
>
> 그리고 strftime()은 한개의 parameter을 가지는데 그것은 구체적으로 어떤 string으로 변신시킬지 적는 것이다

| Directive | Description                                                 | Example                  | Try it                                                       |
| :-------- | :---------------------------------------------------------- | :----------------------- | :----------------------------------------------------------- |
| %a        | Weekday, short version                                      | Wed                      | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_datetime_strftime_a) |
| %A        | Weekday, full version                                       | Wednesday                | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_datetime_strftime_a2) |
| %w        | Weekday as a number 0-6, 0 is Sunday                        | 3                        | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_datetime_strftime_w) |
| %d        | Day of month 01-31                                          | 31                       | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_datetime_strftime_d) |
| %b        | Month name, short version                                   | Dec                      | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_datetime_strftime_b) |
| %B        | Month name, full version                                    | December                 | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_datetime_strftime_b2) |
| %m        | Month as a number 01-12                                     | 12                       | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_datetime_strftime_m) |
| %y        | Year, short version, without century                        | 18                       | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_datetime_strftime_y) |
| %Y        | Year, full version                                          | 2018                     | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_datetime_strftime_y2) |
| %H        | Hour 00-23                                                  | 17                       | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_datetime_strftime_h2) |
| %I        | Hour 00-12                                                  | 05                       | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_datetime_strftime_i2) |
| %p        | AM/PM                                                       | PM                       | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_datetime_strftime_p) |
| %M        | Minute 00-59                                                | 41                       | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_datetime_strftime_m2) |
| %S        | Second 00-59                                                | 08                       | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_datetime_strftime_s2) |
| %f        | Microsecond 000000-999999                                   | 548513                   | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_datetime_strftime_f) |
| %z        | UTC offset                                                  | +0100                    |                                                              |
| %Z        | Timezone                                                    | CST                      |                                                              |
| %j        | Day number of year 001-366                                  | 365                      | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_datetime_strftime_j) |
| %U        | Week number of year, Sunday as the first day of week, 00-53 | 52                       | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_datetime_strftime_u2) |
| %W        | Week number of year, Monday as the first day of week, 00-53 | 52                       | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_datetime_strftime_w2) |
| %c        | Local version of date and time                              | Mon Dec 31 17:41:00 2018 | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_datetime_strftime_c) |
| %x        | Local version of date                                       | 12/31/18                 | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_datetime_strftime_x) |
| %X        | Local version of time                                       | 17:41:00                 | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_datetime_strftime_x2) |
| %%        | A % character                                               | %                        |                                                              |



```python
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))
>> JUNE
```

