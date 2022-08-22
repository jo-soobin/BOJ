num = int(input())

for i in range(num):
    idx, word = input().split()
    idx = int(idx)
    print(word[:idx-1]+word[idx:])