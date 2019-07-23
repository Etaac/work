import random


def CheckA(num, ans):
    # 判斷A的個數
    a = 0
    for i in range(4):
        if num[i] == int(ans[i]):
            a += 1
    return a


def ChechB(num, ans):
    # 判斷B的個數
    b = 0
    for i in range(0, 4):
        for j in range(1, 4):
            if num[i] == int(ans[i - j]):
                b += 1
    return b


def ChechValid(num):
    for i in range(4):
        for j in range(i):
            if num[i] == num[j]:
                return False
    return True


a = 0
value = [i for i in range(0, 10)]
num = []
# 生成四個不一樣的數字
for i in range(4):
    num.append(random.choice(value))
    value.remove(num[i])
print(num)

while a != 4:
    while 1:
        ans_temp = input("請輸入數字:")
        if len(ans_temp) == 4 and ChechValid(ans_temp):
            break
        print('格式錯誤')
    ans = list(ans_temp)
    a = CheckA(num, ans)
    b = ChechB(num, ans)
    print(a, 'A', b, 'B')

print('正確答案')
