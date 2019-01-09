# 조건문
'''
< 조건이 1개 >
if 조건식:
    수행코드

< 조건이 2개 >
if 조건식:
    수행코드
else:
    수행코드

< 조건이 3개 이상 >
if 조건식:
    수행코드
elif 조건식:
    수행코드
else:
    수행코드
'''
print('커피값을 지불해 주세요')

# input() : 콘솔에서 사용자 입력을 받는 함수
# 입력을 하고 엔터키를 칠때까지 Block 상태로 대기
# 사용자가 입력하고 엔터치면 입력값을 리턴한다
# 리턴값의 타입은 문자열로 반환해준다. 
money = int(input()) # 노란색은 내장함수, 초록색은 생성자
COFFIE_PRICE = 2000

# 2000원보다 작으면 적게 입력했다
if money < COFFIE_PRICE :
    # pass : 아무것도 안하고 넘길때 쓰는 명령어, 아예 아무것도 안 쓰면 오류가 나옴
    print('돈이 부족합니다.')
# 2000원과 같으면 정상 지불했다
elif money == COFFIE_PRICE :
    print('정상 결제 되었습니다.')
# 2000원보다 크면 잔돈을 계산해서 잔돈 반환
else:
    money -= COFFIE_PRICE
    print('정상 결제 되었습니다.')
    #print('잔돈은 ' + str(money)+'입니다') 
    print('잔돈은 %s원입니다' % money) 
