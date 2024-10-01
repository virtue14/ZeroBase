str = 'Hi '
result = str * 5
print('result : {}'.format(result))

num1 = 10
num2 = 3
result = num1 / num2
print('result : {}'.format(result))
print('result : %.2f' % result)

num1 = 0
num2 = 3

# result = num2/num1
# print('result : {}'.format(result))
# print('result : %.2f' % result)

num1 = 20
num2 = 5
result = int(num1 / num2)
print('result : {}'.format(result))
print('result : {}'.format(type(result)))

korScore = int(input('국어점수 : '))
engScore = int(input('영어점수 : '))
mathScore = int(input('수학점수 : '))

total = korScore + engScore + mathScore
avgScore = total / 3

print('국어점수 : {}'.format(korScore))
print('영어점수 : {}'.format(engScore))
print('수학점수 : {}'.format(mathScore))
print('총점 : {}'.format(total))
print('평균 : {}'.format(avgScore))
print('평균 : %d' % avgScore)
