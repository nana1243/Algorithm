

def average(array):
    ans = sum(set(array)) / len(set(array))
    return ans


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    result = average(arr)
    print(result)






