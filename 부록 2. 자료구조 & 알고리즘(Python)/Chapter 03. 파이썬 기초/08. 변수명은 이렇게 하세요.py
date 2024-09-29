# 변수 작성법
import keyword

# 영문 사용
# Yes
myAddress = '대한민국 서울시'
print(myAddress)
# No
나의주소 = '대한민국 서울시'
print(나의주소)

# 첫 번째는 소문자로
# Yes
myAddress = '대한민국 서울시'
print(myAddress)
# No
MyAddress = '대한민국 서울시'
print(MyAddress)

# 가급적 데이터의 의미를 파악할 수 있는 명사 사용
# Yes
myWeight = 80
print(myWeight)
# No
mw = 80
print(mw)

#카멜 표가법 또는 스네이크 표기법 사용
# Yes(카멜)
customerBankAccount = '123-01-123456'
print(customerBankAccount)
# Yes(스네이크)
customer_bank_account = '123-01-123456'
print(customer_bank_account)
# No
customerbankaccuout = '123-01-123456'
print(customerbankaccuout)

# 예약어(파이썬에서 이미 예약된 단어) 사용 금지
# (X) import keyword
# (X) print(keyword.kwlist)

# 특수문자 사용금지
# $myWeight = 10

# 공백문자 사용 금지
# my address = 20
#  myAddress = 20
# myAddress  = 20

# 숫자는 사용해도 되지만 첫 번째 사용 금지
# Yes
myAddress1 = 'korea seoul'
# Yes
myAddress1 = 'korea seoul'
# No
# 1myAddress = 'korea seoul'

# Ex
middleExampleScore = 100
print(middleExampleScore, '점')

width = 20
height = 40
area = width * height
print(area)