def solution(genres, plays):
    from collections import Counter
    genres_score=dict()
    for i in range(len(plays)):
        if (genres[i]) in genres_score.keys():
            genres_score[genres[i]]+=plays[i]
        else:
            genres_score[genres[i]]=plays[i]
    ind_genres_plays=[]
    for i in range(len(plays)):
        ind_genres_plays.append((i,genres[i],plays[i]))
    genres_score=sorted(genres_score.items(),reverse=True,key=lambda item: item[1])
    ind_genres_plays=sorted(ind_genres_plays,key=lambda x: x[2], reverse=True)
    
    answer=[]
    for i in range(len(genres_score)):
        cnt=0
        for j in range(len(genres)):
            if genres_score[i][0]==ind_genres_plays[j][1]:
                answer.append(ind_genres_plays[j][0])
                cnt+=1
                if cnt==2:
                    break
    return answer