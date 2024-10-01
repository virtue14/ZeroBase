import math
# 거듭 제곱

num1 = 7
num2 = 5
result = num1 ** num2
print('result: {}'.format(result))

# 제곱근
# 2의 제곱근 구하기
result = 2 ** (1 / 2)
print('2의 제곱근 %f' % result)
print('2의 제곱근 %.2f' % result)

# 2의 3제곱근 구하기
result = 2 ** (1 / 3)
print('2의 3제곱근 %f' % result)
print('2의 3제곱근 %.2f' % result)

# 2의 4제곱근 구하기
result = 2 ** (1 / 4)
print('2의 4제곱근 %f' % result)
print('2의 4제곱근 %.2f' % result)

print(math.sqrt(2))
print(math.sqrt(3))
print(math.sqrt(4))

print(math.pow(2,3))

firstMonthMoney = 200
after12Month = ((firstMonthMoney * 0.01) ** 12) * 100
print('12개월 후 용돈: {}'.format(after12Month))

after12Month = int(after12Month)
strResult = format(after12Month, ',')
print(strResult,'원')