def solution(prices):
    ans = [i for i in range(len(prices) - 1, -1, -1)]
    stack = []

    for idx, cur in enumerate(prices):

        while stack and cur < prices[stack[-1]]:
            last = stack.pop()
            ans[last] = idx - last

        stack.append(idx)

    return ans