def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return len(cities)*5
    Cache = []
    for c in cities:
        i = c.upper()
        if i in Cache:
            answer += 1
            Cache.remove(i)
            Cache.append(i)
        else:
            answer += 5
            if len(Cache) == cacheSize:
                del Cache[0]
            Cache.append(i)
    return answer
