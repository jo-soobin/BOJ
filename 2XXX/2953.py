lst = [list(map(int, input().split())) for i in range(5)]
total = []
for idx in range(5):
    total.append(sum(lst[idx]))

answer1 = total.index(max(total))+1
answer2 = max(total)
print(answer1,answer2)