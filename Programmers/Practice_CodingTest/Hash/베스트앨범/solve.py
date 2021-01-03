def solution(genres, plays):
    ml = {}
    ml4cnt = {}
    for i in range(len(genres)):
        if genres[i] in ml.keys():
            ml[genres[i]].append((plays[i], i))
            ml4cnt[genres[i]] += plays[i]
        else:
            ml[genres[i]] = [(plays[i], i)]
            ml4cnt[genres[i]] = plays[i]
    answer = []
    for i in sorted(ml4cnt.items(), key=lambda x: x[1], reverse=True):
        for j in sorted(ml[i[0]], key=lambda x: (-x[0], x[1]))[:2]:
            answer.append(j[1])
    return answer


testcase1 = ['A', 'B', 'A', 'A', 'B']

testcase2 = [50, 60, 15, 80, 250]

print(solution(testcase1, testcase2))
