num1 = 10
num2 = 3

result = num1 % num2
print(result)

result = num1 // num2
print(result)

result = divmod(num1, num2)
print('result : {}'.format(result))

print('몫 : {}'.format(result[0]))
print('나머지 : {}'.format(result[1]))

allStuCnt = int(input('전체 학생의 수: '))
stuCntOfGroup = int(input('한 모둠 학생의 수: '))
groupCnt = allStuCnt // stuCntOfGroup
overStuCnt = allStuCnt % stuCntOfGroup
print('전체 학생 수: {}'.format(allStuCnt))
print('한 모둠 학생의 수: {}'.format(groupCnt))
print('모둠 수: {}'.format(groupCnt))
print('남는 학생 수: {}'.format(overStuCnt))

result = divmod(allStuCnt, stuCntOfGroup)
print(result)
print('몫 : {}'.format(result[0]))
print('나머지 : {}'.format(result[1]))