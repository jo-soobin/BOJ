case = int(input())
for i in range(case):
    scores = [int(i) for i in input().split()]
    student = scores[0]
    scores = scores[1:]

    avg = sum(scores)/student

    count = 0
    for score in scores:
        if score > avg:
            count += 1
    
    print(f'{(count/student)*100:.3f}%')