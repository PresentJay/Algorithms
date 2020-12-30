def solution(genres, plays):
    ml = {}
    mlc = {}
    for i in range(len(genres)):
        if genres[i] in ml.keys():
            ml[genres[i]].append([plays[i], i])
            mlc[genres[i]] += plays[i]
        else:
            ml[genres[i]] = [[plays[i], i]]
            mlc[genres[i]] = plays[i]

    res = {}
    answer = []
    for s in sorted(mlc.items(), key=lambda sum: sum[1], reverse=True):
        for i in sorted(ml[s[0]], reverse=True)[:2]:
            if str(i[0]) in res.keys():
                res[str(i[0])].append(i[1])
                res[str(i[0])].sort()
            else:
                res[str(i[0])] = [i[1]]

    for i in sorted(res.items(), key=lambda id: id[0], reverse=True):
        for j in i[1]:
            answer.append(j)
    return answer


testcase1 = ['A', 'B', 'A', 'A', 'B']
testcase2 = [50, 60, 15, 80, 250]

print(solution(testcase1, testcase2))
