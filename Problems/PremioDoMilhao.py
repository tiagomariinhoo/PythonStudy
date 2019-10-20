n = int(input())
vec = [int(input()) for i in range(n)]

sum = 0

for i in range(len(vec)):
    sum += vec[i]
    if(sum >= int(1e6)):
        print(i+1)
        break
