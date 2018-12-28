'''
< 숫자 맞추기 게임 >
자료형, 조건문, 반복문만 이용하여 게임을 구현한다
함수x,객체지향적x,오직 절차지향적 프로그래밍 사용
0 ~ 99까지 랜덤으로 나오는 값을 찾는 머드 게임( 텍스트를 주고 받으면서 숫자를 맞추는 게임 )
'''

# STEP1
# 게임의 제목을 입력하세요 프롬프트 출력
# 적당한 (영문)제목이 입력되면 다음 단계 진행
# print('게임의 제목을 입력하세요.')
# game_title = input()
# \n : 줄바꿈 처리
# game_title = input('게임의 제목을 입력하세요.\n')

#   STEP 1-1
#   게임 제목은 28자 이내로 입력받는다
#   1) 입력하지 않으면  '게임 제목이 입력되지 않았습니다. 다시 입력하세요.' 
#   2) 많으면 에러 띄우고 '게임 제목이 28자를 초과합니다. 다시 입력하세요.'
#   3) 28자 이내면 OK
while True: # 무한루프 반드시 break 를 사용해서 탈출해야함
    game_title = input('게임의 제목을 입력하세요.\n')
    # if len(game_title) == 0: 아래와 같은 경우
    if not game_title: # 입력하지 않는 경우 -> not을 이용해서
        print('게임 제목이 입력되지 않았습니다. 다시 입력하세요.')
    elif len(game_title) > 28: #28자를 초과하는 경우
        print('게임 제목이 28자를 초과합니다. 다시 입력하세요.')
    else: # 1글자 이상 28자 이내인 경우 ok
        break

# STEP2
# ========================================
# =              게임제목                  =
# =              v 0.0.1                 = 
# ========================================


# STEP3
# 게이머의 이름을 입력하세요
# -> 이름을 넣지 않으면 뭐라 하고 다시 입력

# STEP4
# AI의 숫자를 입력하라고 프롬프트 출력
# 숫자를 입력하지 않으면 '경고메세지' 출력
# 숫자가 아닌 값을 넣으면 '경고 메세지' 다시 입력
# 0보다 작거나, 100 이상의 값을 입력하면 '경고메세지' 다시 입력
# 정상 범위에 있는 정수값을 입력하면 다음 단계 진행

# STEP5
# AI는 숫자를 하나 생성한다 ( 랜덤 ) -> 1회만 생성
# 즉 게임 한번이 종료될때까지 유지되어야 한다

# STEP6
# 판단
# 1) 입력값이 정답보다 작으면 => 작다라고 출력!
# 2) 입력값이 정답보다 크면 => 크다고 출력!
# 3) 입력값이 정답과 동일하면 => 정답! 축하메세지!

# STEP7
# 결과 표시
# 총 시도 횟수, 점수(10-총시도횟수)*10를 표시
# 다시 게임을 하시겠습니까?
# YES (대소문자 구분안함) -> STEP4으로
# NO (대소문자 구분안함) -> 프로그램 종료
# 아무것도 입력하지 않아도 경고 메세지
# 입력값이 틀려도 경고 메세지  
