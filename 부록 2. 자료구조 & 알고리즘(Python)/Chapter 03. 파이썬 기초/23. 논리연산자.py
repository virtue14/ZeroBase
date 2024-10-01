print('{} & {}: {}'.format(True, True, (True & True)))
print('{} & {}: {}'.format(True, False, (True & False)))
print('{} & {}: {}'.format(False, True, (False & True)))
print('{} & {}: {}'.format(False, False, (False & False)))

print('{} | {}: {}'.format(True, True, (True | True)))
print('{} | {}: {}'.format(True, False, (True | False)))
print('{} | {}: {}'.format(False, True, (False | True)))
print('{} | {}: {}'.format(False, False, (False | False)))

print('not {} : {}'.format(True, (not True)))
print('not {} : {}'.format(False, (not False)))

age = int(input('나이 입력: '))
vaccine = (age < 20) | (age >= 65)
print('age: {}, vaccine: {}'.format(age, vaccine))

passScore1 = 60
passScore2 = 70

korScore = int(input('국어점수: '))
engScore = int(input('영어점수: '))
mathScore = int(input('수학점수: '))

scoreAvg = (korScore + engScore + mathScore) / 3
scoreAvgResult = scoreAvg >= passScore2

korResult = korScore >= passScore1
engResult = engScore >= passScore1
mathResult = mathScore >= passScore1

subjectResult = korResult and engResult & mathResult
print('평균: {}, 결과: {}'.format(scoreAvg, scoreAvgResult))
print('국어: {}, 결과: {}'.format(korScore, korResult))
print('영어: {}, 결과: {}'.format(engScore, engResult))
print('수학: {}, 결과: {}'.format(mathScore, mathResult))
print('과락 결과: {}'.format(subjectResult))

print('최종 결과: {}'.format(scoreAvgResult and subjectResult))