# stack
>LIFO (Last Input First Out, 선입후출, 라이포)
>데이터 저장소에서 새로 들어오는 데이터의 위치가 저장소의 끝 부분(Top 혹은 Top pointer라고 한다)이고, 
>내보내는 데이터 역시 저장소의 Top에서 나간다. 입력은 push, 출력은 pop이다. 
>peek는 Top의 위치에 있는 데이터를 확인하는 것을 말한다.


![stack_LIFO](C:\Users\user\Pictures\DataStructure\stack_LIFO.PNG)







### stack ADT (인터페이스)

- **is_empty()** -> boolean
- **push** -> insert : push(data)
- **pop** -> delete : pop return 맨위 값을 리턴하고 동시에 삭제
- **peek** -> 엿보기 : 맨 위 값 반환만 하고 삭제는 안함

### stack 구현 예시1 (python list 사용)

>```python
>class stack(list):
>    def push(self,object):
>        return self.append(object)
>
>    def is_empty(self):
>        if not self :
>            return True
>        else:
>            return False
>
>    def peek(self):
>        return self[-1]
>
>    def print(self):
>        return self
>
>
>```
>
>
>
>

### stack 구현예시 (python )

