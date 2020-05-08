#
# # 이문제는 부정방정식 문제
#
# N,K=map(int,input().split(" "))
# coin=[]
# for i in range(N):
#     c=map(int,input())
#     coin.append(c)
#
# ###############################
#
# ## ax+by+cz=k가 되면 ans에 넣는다
#
# coin.sort(reverse=True)
# ans=0
# # 가장 큰수의 몫부터 시작한다 (몫, 0 ,0)
# def recur(coin,K,ans):
#     n=K//coin[0]
#     result=(0 for i in range(N))
#     while n>=0:
#         if K%coin[0]==0:
#             ans+=1
#             n=K//coin[0]-1
#         K-=(K//coin[0]-1)*coin[0]
#         return
#     else:
#
#
#
#
#
#
#
#
