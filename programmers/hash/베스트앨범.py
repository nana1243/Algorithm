genres=["classic", "pop", "classic", "classic", "pop"]
plays=[500, 600, 150, 800, 2500]
# return=[4, 1, 3, 0]
from collections import Counter
# 장르별 어떤 장르가 가장 많이 들었는지 순서대로
genres_score=dict()

for i in range(len(plays)):
    if (genres[i]) in genres_score.keys():
        genres_score[genres[i]]+=plays[i]
    else:
        genres_score[genres[i]]=plays[i]
ind_genres_plays=[]
for i in range(len(plays)):
    ind_genres_plays.append((i,genres[i],plays[i]))


genres_score=sorted(genres_score,reverse=True)
ind_genres_plays=sorted(ind_genres_plays,key=lambda x: x[2], reverse=True)
answer=[]
for i in range(len(genres_score)):
    cnt=0
    for j in range(len(genres)):
        if genres_score[i]==ind_genres_plays[j][1]:
            answer.append(ind_genres_plays[j][0])
            cnt+=1
            if cnt==2:
                break

print(answer)
