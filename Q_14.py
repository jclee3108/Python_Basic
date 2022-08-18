from collections import deque

scoville = [1, 2, 3, 9, 10, 12]	
K = 7 

scoville.sort() 

sum = 0
cnt = 0 

while sum >= K:
    sum = scoville.popleft()
    sum = sum + ( scoville.popleft() * 2 ) 

    scoville.pop(0)
    scoville.pop(0)

    scoville.append(sum)

    scoville.sort()

    print(scoville)
    
    cnt += 1 
    
    if sum >= K:
        break


print(cnt)




