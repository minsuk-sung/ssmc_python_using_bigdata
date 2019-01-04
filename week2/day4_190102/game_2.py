'''
game_1.py는 절차적 프로그래밍이다
좀더 효율성과 확정성, 재사용성을 위해서
함수 지향적 프로그램으로 마이그레이션(이주) 진행하자
-> 시작점 존재(시작함수 존재)
'''

class NMG:

    # 1. 멤버변수

    game_title = ''
    titlelen = 0
    player_name = ''
    game_info = [game_title, 'v 1,0,0','MADE BY SSMC','THANK YOU']
    ai_value = 0
    try_count = 0
    game_on = True
    game_input = 0
    game_flag_ans = True
    game_flag_input = True

    # 2. 멤버함수

    # STEP1
    # 게임 제목의 길이 제한을 인자로 받아서 확장성을 높인다
    def step1(self,titlelen):
        self.titlelen = titlelen
        while True: # 무한루프 반드시 break 를 사용해서 탈출해야함
            game_title = input('%d자 이내의 게임의 제목을 입력하세요.\n' % self.titlelen)
            # if len(game_title) == 0: 아래와 같은 경우
            if not game_title: # 입력하지 않는 경우 -> not을 이용해서
                print('게임 제목이 입력되지 않았습니다. 다시 입력하세요.')
            elif len(game_title) > titlelen: #28자를 초과하는 경우
                print('게임 제목이 %d자를 초과합니다. 다시 입력하세요.' % self.titlelen)
            else: # 1글자 이상 28자 이내인 경우 ok
                self.game_info[0] = game_title
                break
    
    # STEP2
    # 입력한 게임의 제목과 함께 게임의 정보를 출력한다 
    def step2(self):
        print('='*self.titlelen)
        txt = '={0:^%s}=' % (self.titlelen-2)
        for t in self.game_info:
            print(txt.format(t))
        print('='*self.titlelen)

    # STEP3
    # 플레이어의 이름을 입력받는 부분
    def step3(self):
        flag = True
        while flag:
            player_name = input('게이머의 이름을 입력하세요 : \n')
            if not player_name:
                print('게이머의 이름을 정확하게 입력하지 않으셨습니다.')
                continue # 이렇게 된다면 다시 위로 올라가므로 else 가 필요없어짐
        #   else:
            self.player_name = player_name
            flag = False
    
    # STEP4
    def step4(self):
        self.ai_value = 0
        while self.game_flag_ans: # 사용자가 AI값을 맞출때까지 반복
            while True: # 사용자가 숫자를 입력하는 반복
                # 공백 제거를 해서 오동작을 방지
                print('= '*40)
                if self.try_count >= 10:
                    print('10번 이상 시도하셨습니다.')
                    self.game_flag_ans = False
                    return 
                game_input = input('AI의 숫자(0~99)를 입력하세요.\n').strip()
                if not game_input: # 숫자를 넣지 않으면
                    print('입력을 정확하게 하세요')
                elif not game_input.isnumeric(): #숫자가 아닌 값을 넣으면
                    print('0~99사이의 정수값을 입력하세요')
                else:
                    game_input = int(game_input)
                    if game_input >= 0 and game_input < 100:
                        self.game_input = game_input
                        break
                    print('적절한 정수값을 입력하세요')
            self.try_count += 1 # try_count = try_count + 1
            print('= '*40)
            print('{0}번 시도 했습니다.'.format(self.try_count))


            # STEP5
            # AI는 숫자를 하나 생성한다 ( 랜덤 ) -> 1회만 생성
            # 즉 게임 한번이 종료될때까지 유지되어야 한다
            # 모듈 가져오기 ( 다른 사람이 만든 라이브러리 이해 )
            # 파이썬은 모듈,패키지 밖에 없다 
            import random
            if not self.ai_value: # ai 값이 세팅되어 있지 않았다면 (딱 한번만 세팅해주기 위해서)
                self.ai_value = random.randint(0,99) # 그럴 경우에는 세팅해라
                # print("AI : {0}".format(self.ai_value))

            # STEP6
            # 판단
            # 1) 입력값이 정답보다 작으면 => 작다라고 출력!
            # 2) 입력값이 정답보다 크면 => 크다고 출력!
            # 3) 입력값이 정답과 동일하면 => 정답! 축하메세지! => STEP7
            if self.game_input < self.ai_value:
                print('입력값이 작습니다')
            elif self.game_input > self.ai_value:
                print('입력값이 큽니다')
            else:
                print('정답입니다!')
                self.game_flag_ans = False
    
    # STEP7
    def step7(self):
        prompt = ''' = = = = = = = = = = = = = =\n총 시도 횟수 : %s\n점수 : %s\n다시 게임하시겠습니까?(YES/NO)\n= = = = = = = = = = = = = =\n> ''' % (self.try_count,(10 - self.try_count)*10)
        while True:
            result = input(prompt).strip().upper()
            if not result:
                print('YES / NO 중 하나를 입력하세요')
            elif result == 'NO':
                print('Bye Bye!')
                self.game_on = False
                break
            elif result == 'YES':
                print('Game Restart')
                self.game_flag_ans = True
                self.try_count = 0
                break
            else:
                print('제대로 입력해주세요')

    # 3. 생성자 함수
    def __init__(self):
        self.try_count = 0

def main():
    game = NMG()
    game.step1(28)
    game.step2()
    game.step3()
    while game.game_on:
        game.step4()
        game.step7()

# 이 코드를 중심으로 구동될때만 main을 호출하고 싶다
if __name__ == '__main__':
    main()