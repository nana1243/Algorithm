from collections import deque

def LRU(cacheSize, cities):
    ans = 0
    cache = deque([])
    limit = 0
    for elm in cities:
        if len(cache) > cacheSize:
            cache.popleft()
        if elm in cache:
            ans += 1
            cache.remove(elm)
        else:
            ans += 5
        cache.append(elm)
    return ans


def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    cities = [elm.lower() for elm in cities]

    answer = LRU(cacheSize, cities)
    return answer