# # 1부터 10,000까지 9이라는 숫자가 총 몇번 나오는가?

# list = str(list(range(1,10001)))

# print (list.count('8'))

#################################################

# # 1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오. (단 점들의 배열은 모두 정렬되어있다고 가정한다.)
# # 예를들어 S={1, 3, 4, 8, 13, 17, 20} 이 주어졌다면, 결과값은 (3, 4)가 될 것이다.

# s = [1, 3, 4, 8, 13, 17, 20]
# m = max(s)
# result = []

# index = 0 

# for i in range(len(s) -1):
#     if m > abs(s[i + 1] - s[i]): 
#         m = abs(s[i + 1] - s[i])
#         result = []
#         result.append(s[index])
#         result.append(s[index + 1])

#     index += 1 

# print(result)

#################################################

s = [1, 3, 4, 8, 13, 17, 20]
ss = [3, 4, 8, 13, 17, 20]

# s = [1, 3, 4, 8, 13, 17, 20]
# ss = [4, 3, 8, 13, 17, 20]

# 2개의 리스트 합치기
list_total = list(zip(s,ss))

# i[0] 은 s 리스트 
# i[1] 은 ss 리스트 
# sorted(list_total, key=lambda i: i[1]- i[0])

# i[1] - i[0] 로 정렬 후 첫번째 리스트 값 보여주기 
result = list(sorted(list_total, key=lambda i: i[1]- i[0])[0]) 

# print( list(sorted(list_total, key=lambda i: i[1]- i[0])[0]) )
# result = list(sorted(list_total, key=lambda i: i[1]- i[0])[0]) 
print(result)
