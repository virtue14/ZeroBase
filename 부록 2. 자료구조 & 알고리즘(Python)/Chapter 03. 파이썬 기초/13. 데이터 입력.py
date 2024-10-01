print('키보드를 통해서 데이터를 입력하세요.')
userInputData = input()
print(userInputData)

userInputData = input('키보드를 통해서 데이터를 입력하세요\n')
print(userInputData)

userInputData = input()
print(userInputData)
print(type(userInputData))

userInputData = input('문자를 입력하세요.')
print(userInputData)
print(type(userInputData))

userInputData = int(input('숫자를 입력하세요.'))
print(userInputData)
print(type(userInputData))

userInputData = float(input('실수를 입력하세요.'))
print(userInputData)
print(type(userInputData))

userInputData = bool(input('논리형을 입력하세요.'))
print(userInputData)
print(type(userInputData))

userInputData = input('오늘 날씨 정보 입력 : ')
print(userInputData)

width = int(input('가로 길이 입력 : '))
height = int(input('세로 길이 입력 : '))
area = width * height
print(area)
print(area/2)

userName = input('이름을 입력하세요 : ')
print('안녕하세요, ' + userName + '님!')