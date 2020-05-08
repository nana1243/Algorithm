#### 효율성(다맞음)25+정확성50(10/15개 맞음)


### dp_카드게임문제
# https://programmers.co.kr/learn/courses/30/lessons/42896
def solution(left, right):
    ans=0
    ### 왼쪽카드를 max전까지 다 버렸다고 가정햇을때, 왼쪽 max의 값을 구함
    mleft=max(left)
    ##### 그리고 right의 원소중에서 max보다 작으면 ans+=element로 해서 점수를 얻는 방식으로 문제를 풀음
    for element in right:
        if element<mleft:
            ans+=element
    return ans

### 아마 테스트 케이스에서 통과가 안되는 것이 max이후에 right의 숫자가 큰 숫자가 나타날때
### 거기서 문제가 나타나는 것 같은데 ㅜㅜㅜㅜ 이방법으로
### 문제를 풀 수 없을까? ㅜㅜㅜㅜㅜ