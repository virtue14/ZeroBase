from openpyxl.styles.builtins import total

num1 = 10
num2 = 20
result = num1 + num2
print(result)

num = 10
num += 3
print('num: {}'.format(num))

num = 10
num -= 3
print('num: {}'.format(num))

num = 10
num *= 3
print('num: {}'.format(num))

num = 10
num %= 3
print('num: {}'.format(num))

num = 10
num //= 3
print('num: {}'.format(num))

num = 10
num **= 3
print('num: {}'.format(num))

rainAmount = 0
totalRainAmount = 0

totalRainAmount += 30
print('1월 누적 강수량: {}mm'.format(totalRainAmount))

totalRainAmount += 45
print('2월 누적 강수량: {}mm'.format(totalRainAmount))

totalRainAmount += 47
print('3월 누적 강수량: {}mm'.format(totalRainAmount))

totalRainAmount += 55
print('4월 누적 강수량: {}mm'.format(totalRainAmount))

totalRainAmount += 65
print('5월 누적 강수량: {}mm'.format(totalRainAmount))

totalRainAmount += 100
print('6월 누적 강수량: {}mm'.format(totalRainAmount))

totalRainAmount += 128
print('7월 누적 강수량: {}mm'.format(totalRainAmount))

totalRainAmount += 209
print('8월 누적 강수량: {}mm'.format(totalRainAmount))

totalRainAmount += 204
print('9월 누적 강수량: {}mm'.format(totalRainAmount))

totalRainAmount += 186
print('10월 누적 강수량: {}mm'.format(totalRainAmount))

totalRainAmount += 67
print('11월 누적 강수량: {}mm'.format(totalRainAmount))

totalRainAmount += 25
print('12월 누적 강수량: {}mm'.format(format(totalRainAmount, ',')))

rainAvgAmount = totalRainAmount / 12

print('-' * 30)
print('연간 누적 강수량: {}'.format(totalRainAmount))
print('연간 평균 강수량: {}'.format(rainAvgAmount))
print('-' * 30)
