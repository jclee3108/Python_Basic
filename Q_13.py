from collections import deque

s = "(())()"

answer = True

# if len(s)%2 != 0:
#     answer = False

# s_cnt = len(s)/2



# for i in range(1,int(s_cnt)+1):
#     s = s.replace("()","")
#     # print(i)

# if s == "":
#     answer = True 
# else:
#     answer = False

# print(answer)


deq = deque(s)

while deq == []:
    x = deq.popleft()
    print(x)

# print(deq)

