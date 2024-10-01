char1 = 'A'  # 65
char2 = 'S'  # 83
print('\'{}\' > \'{}\': {}'.format(char1, char2, (char1 > char2)))
print('\'{}\' >= \'{}\': {}'.format(char1, char2, (char1 >= char2)))
print('\'{}\' < \'{}\': {}'.format(char1, char2, (char1 < char2)))
print('\'{}\' <= \'{}\': {}'.format(char1, char2, (char1 <= char2)))
print('\'{}\' == \'{}\': {}'.format(char1, char2, (char1 == char2)))
print('\'{}\' != \'{}\': {}'.format(char1, char2, (char1 != char2)))

print('-' * 30)

print('\'A\' -> {}'.format(ord('A')))
print('\'a\' -> {}'.format(ord('a')))
print('\'S\' -> {}'.format(ord('S')))
print('\'s\' -> {}'.format(ord('s')))

print('-' * 30)

print('65 -> {}'.format(chr(65)))
print('83 -> {}'.format(chr(83)))

print('-' * 30)

str1 = 'Hello'
str2 = 'hello'
print('{} == {}: {}'.format(str1, str2, (str1 == str2)))
print('{} != {}: {}'.format(str1, str2, (str1 != str2)))

print('-' * 30)

userInputAlphabet = input('알파벳 입력: ')
print('{} : {}'.format(userInputAlphabet, ord(userInputAlphabet)))

print('-' * 30)

userInputASCII = int(input('아스키 코드 입력: '))
print('{} : {}'.format(userInputASCII, chr(userInputASCII)))