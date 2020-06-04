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






    ######################### 풀이2#####################
  
    g={elm :0 for elm in genres }
    for i in range(len(plays)):
        g[genres[i]]=g[genres[i]] + plays[i]
    g = sorted(g.keys(), key=lambda x: g[x], reverse=True)
    p=[]
    for i,j in enumerate(zip(genres,plays)):
        idx=i
        genre=j[0]
        play=j[1]
        p.append((genre,play,idx))
    p.sort(key =lambda x:x[1],reverse=True)
    ans=[]
    for i in range(len(g)):
        cnt=0
        for element in p:
            if element[0]==g[i] :
                cnt+=1
                ans.append(element[2])
            if cnt==2:
                break
    return ans