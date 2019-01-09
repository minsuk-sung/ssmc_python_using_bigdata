import random

print(random.randint(0,100))

# 특정 문자열이 숫자임을 체크
txt = ['1','A','a','!','가','3.14']
# print('1'.isalpha())
# print('1'.isdecimal())
# print('1'.isdigit())
# print('1'.isnumeric())

for t in txt:
    print(t,t.isalpha(), # 알파벳인지 이런 내장함수들은 모두 string 형태여야 하는구나
            t.isdecimal(), # 10진수인지
            t.isdigit(), # 숫자인지
            t.isnumeric()) # 숫자인지

# # 참인 케이스를 잡고 아닌 것 나머지 처리
# a = ''
# if a:
#     print('1')
# else:
#     print('2') # 정답

# # 거짓인 케이스를 잡고 아닌 것 나머지 처리
# a = '22'
# if not a: # 비어있다면 참이었겠지
#     print('1')
# else:
#     print('2') # 정답 : 왜냐하면 a가 비지 않은게 아니니까