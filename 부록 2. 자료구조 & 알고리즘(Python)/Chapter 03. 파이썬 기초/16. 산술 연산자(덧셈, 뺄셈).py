num1 = 10
num2 = 20

print(num1 + num2)

num1 = 3.14
num2 = 0.12
print('num1 + num2 = %.2f' % (num1 + num2))

str1 = 'Good'
str2 = ' '
str3 = 'morning'
print(str3 + str2 + str1)

num1 = 10
str1 = 'morning'
# print(num1 + str1)

korScore = int(input('국어 점수: '))
engScore = int(input('영어 점수: '))
matScore = int(input('수학 점수: '))

totalScore = korScore + engScore + matScore
print('국어 점수 : {}'.format(korScore))
print('영어 점수 : {}'.format(engScore))
print('수학 점수 : {}'.format(matScore))
print('합계 : {}'.format(totalScore))

partTimeMoney = int(input('알바비 : '))
cardMoney = int(input('카드값 : '))
result = partTimeMoney - cardMoney

print('알바비 : {}'.format(partTimeMoney))
print('카드값 : {}'.format(cardMoney))
print('남은돈 : {}'.format(result))