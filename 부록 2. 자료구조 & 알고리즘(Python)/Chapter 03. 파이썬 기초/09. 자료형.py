# 자료형(Data Type)
# - 효율적인 메모리 사용을 위해서 데이터를 정수형, 실수형, 문자(열)형, 놀리형으로 구분한 것.

# 정수 : int
num = 10
score = 85

# 실수 : float
pi = 3.14
height = 180.5

# 문자(열) : str
intro = '안녕하세요'
country = 'korea'

# 논리형 : bool
exampleResult = True
dayOff = False

# 정수는 메모리가 허용되는 한 무한 사용 가능.
num = 12345678901234567890
print(num)

# 실수는 대략 소수점 이하 17 ~ 18번째에서 데이터 손실이 일어남.
fNum = 0.12345678901234567890
print(fNum)

score = 100
pi = 3.14
wantGo = '캐나다'
adult = True

var = 3.14
print(type(var))
var = '3.14'
print(type(var))
var = True
print(type(var))
var = 'True'
print(type(var))