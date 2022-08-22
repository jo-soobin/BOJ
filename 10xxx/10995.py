num = int(input())
if num == 1:
    print('*')
else:
    for i in range(num):
        if i%2 == 0:
            print('* '*num)
        elif i%2 != 0:
            print(' *'*num)