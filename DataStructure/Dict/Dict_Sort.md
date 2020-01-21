### DICT의 SORT

1. Key값에따른 오름차순
2. Key값에 따른 내림차순
3.  Value 값에 따른 오름차순
4.  Value값에 따른 내림차순



##### 1. key값에 따른 오름차순

```python
# 기존의 dict의 변수를 d 라고 가정하자

d=sorted(d.items(), key= lambda item :item[0])
```

###### 2. key값에 따른 내림차순

```python
d=sorted(d.items(),key=lambda item:item[0],reverse=True)
```

#### 3. Value 값에 따른 오름차순

```python
d=sorted(d.items(), key=lambda item:item[1])
```

##### 4. Value 값에 따른 내림차순

````python
d=sorted(d.items(), key=lambda item:item[1], reverse=True)
````

