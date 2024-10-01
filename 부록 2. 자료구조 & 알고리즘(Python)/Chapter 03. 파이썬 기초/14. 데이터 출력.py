userName = 'Hong Gil Dong'
print(userName)

userAge = 20
print(userAge)

print('User name : ', userName)
print('User age : ', userAge)
print('User name : ', userName, ', User age : ', userAge)

print('3 * 6 = ', (3*6), end='')
print(3*4)

print(f'User name : {userName}')
print(f'User age : {userAge}')
print(f'User name : {userName}, User age : {userAge}')

print(f'User name : {userName}, \nUser age : {userAge}')
print(f'User name:\t{userName}, \nUser age:\t{userAge}')

width = int(input('가로 길이 : '))
height = int(input('세로 길이 : '))

triangle = width * height / 2
print(f'width: {width}, height: {height}, triangle: {triangle}')
