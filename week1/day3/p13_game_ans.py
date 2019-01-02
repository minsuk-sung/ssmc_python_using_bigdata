'''
< 숫자 맞추기 게임 >
자료형, 조건문, 반복문만 이용하여 게임을 구현한다
함수x,객체지향적x,오직 절차지향적 프로그래밍 사용
0 ~ 99까지 랜덤으로 나오는 값을 찾는 머드 게임( 텍스트를 주고 받으면서 숫자를 맞추는 게임 )
'''
show_all_detail = False
if show_all_detail:
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
    # 
    #   의도가 입력하지 않거나(or) 28자가 넘으면 '게임 입력이 부정확합니다' 라면
    #   if not game_title or len(game_title) > 28:
    #       print('게임 입력이 부정확합니다') 
    #   이런 식으로 작성해야한다.  
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
    # TITLE_LEN = 30
    # print('='*TITLE_LEN)
    # txt = '={0:^%s}=' % (TITLE_LEN-2)
    # print(txt.format(game_title))
    # print(txt.format('v 1.0.0'))
    # print('='*TITLE_LEN)
    TITLE_LEN = 30
    print('='*TITLE_LEN)
    txt = '={0:^%s}=' % (TITLE_LEN-2)
    data = [game_title, 'v 1,0,0','MADE BY SSMC','THANK YOU']
    for t in data:
        print(txt.format(t))
    print('='*TITLE_LEN)

    # STEP3
    # 게이머의 이름을 입력하세요
    # -> 이름을 넣지 않으면 뭐라 하고 다시 입력
    flag = True
    while flag:
        gamer_name = input('게이머의 이름을 입력하세요 : \n')
        if not gamer_name:
            print('게이머의 이름을 정확하게 입력하지 않으셨습니다.')
            continue # 이렇게 된다면 다시 위로 올라가므로 else 가 필요없어짐
    #   else:
        flag = False

# 개발 시간 단축을 위해 해당 변수값ㅇ르 미리 세팅하여 여기서부터 시작
game_title = 'number match game'
gamer_name = 'multi'
game_info = '''
게임 제목 : %s
플레이어 이름 : %s
''' % (game_title,gamer_name)
print(game_info)

# STEP4
# AI의 숫자를 입력하라고 프롬프트 출력
# 숫자를 입력하지 않으면 '경고메세지' 출력 -> 
# 숫자가 아닌 값을 넣으면 '경고 메세지' 다시 입력 -> isnumeric()
# 0보다 작거나, 100 이상의 값을 입력하면 '경고메세지' 다시 입력 -> or 쓰자
# 정상 범위에 있는 정수값을 입력하면 다음 단계 진행
# 게임 시도 횟수를 저장하는 변수
game_on = True
while game_on: # 게임 전체를 반복하기 위해서
    ai_value = 0
    try_count = 0
    while True: # 사용자가 AI값을 맞출때까지 반복
        while True: # 사용자가 숫자를 입력하는 반복
            # 공백 제거를 해서 오동작을 방지
            game_input = input('AI의 숫자(0~99)를 입력하세요.\n').strip()
            if not game_input: # 숫자를 넣지 않으면
                print('입력을 정확하게 하세요')
            elif not game_input.isnumeric(): #숫자가 아닌 값을 넣으면
                print('0~99사이의 정수값을 입력하세요')
            else:
                game_input = int(game_input)
                if game_input >= 0 and game_input < 100:
                    break
                print('적절한 정수값을 입력하세요')
        try_count += 1 # try_count = try_count + 1
        print('{0}번 시도 했습니다.'.format(try_count))


        # STEP5
        # AI는 숫자를 하나 생성한다 ( 랜덤 ) -> 1회만 생성
        # 즉 게임 한번이 종료될때까지 유지되어야 한다
        # 모듈 가져오기 ( 다른 사람이 만든 라이브러리 이해 )
        # 파이썬은 모듈,패키지 밖에 없다 
        import random
        if not ai_value: # ai 값이 세팅되어 있지 않았다면 (딱 한번만 세팅해주기 위해서)
            ai_value = random.randint(0,99) # 그럴 경우에는 세팅해라
            print("AI : {0}".format(ai_value))

        # STEP6
        # 판단
        # 1) 입력값이 정답보다 작으면 => 작다라고 출력!
        # 2) 입력값이 정답보다 크면 => 크다고 출력!
        # 3) 입력값이 정답과 동일하면 => 정답! 축하메세지! => STEP7
        if game_input < ai_value:
            print('입력값이 작습니다')
        elif game_input > ai_value:
            print('입력값이 큽니다')
        else:
            print('정답입니다!')
            break
            

    # STEP7
    # 결과 표시
    # 총 시도 횟수, 점수(10-총시도횟수)*10를 표시
    # 다시 게임을 하시겠습니까?
    # YES (대소문자 구분안함) -> STEP4으로
    # NO (대소문자 구분안함) -> 프로그램 종료
    # 아무것도 입력하지 않아도 경고 메세지
    # 입력값이 틀려도 경고 메세지
    prompt = ''' 

총 시도 횟수 : %s
점수 : %s
다시 게임하시겠습니까?(YES/NO)

''' % (try_count,(10-try_count)*10)
    while True:
        result = input(prompt).strip().upper()
        if not result:
            print('YES / NO 중 하나를 입력하세요')
        elif result == 'NO':
            print('Bye Bye!')
            game_on = False
            break
        elif result == 'YES':
            print('Game Restart')
            break
        else:
            print('제대로 입력해주세요')