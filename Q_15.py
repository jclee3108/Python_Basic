
n=7
n1 = 1 
n2 = 2 

answer = 0 
for i in range(3,n+1):
    answer = (n1+n2) % 1000000007
    n1 = n2
    n2 = answer

print(answer)


print(list(range(3,8)))