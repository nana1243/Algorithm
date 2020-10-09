def solution(number, k):
    # len(number)-k만큼의 자릿수가 보장되어야 한다
    answer = ""
    length = len(number) - k
    while (k >= 1):
        tmp = max(map(int, list(number[:length])))
        put = str(tmp)
        answer += put
        idx = number.index(put)
        k -= idx - 1
        number = number[idx + 1:]
        length -= k

    return answer