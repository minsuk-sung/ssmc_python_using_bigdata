'''
game_1.py는 절차적 프로그래밍이다
좀더 효율성과 확정성, 재사용성을 위해서
함수 지향적 프로그램으로 마이그레이션(이주) 진행하자
-> 시작점 존재(시작함수 존재)
'''

class NMG:

    # 멤버변수
    game_title = ''
    player_name = ''
    game_info = [game_title, 'v 1,0,0','MADE BY SSMC','THANK YOU']

    # 멤버함수
    # STEP1
    # 게임 제목의 길이 제한을 인자로 받아서 확장성을 높인다
    def step1(self,titlelen):
        while True: # 무한루프 반드시 break 를 사용해서 탈출해야함
            self.game_title = input('%d자 이내의 게임의 제목을 입력하세요.\n' % titlelen)
            # if len(game_title) == 0: 아래와 같은 경우
            if not self.game_title: # 입력하지 않는 경우 -> not을 이용해서
                print('게임 제목이 입력되지 않았습니다. 다시 입력하세요.')
            elif len(self.game_title) > titlelen: #28자를 초과하는 경우
                print('게임 제목이 %d자를 초과합니다. 다시 입력하세요.' % titlelen)
            else: # 1글자 이상 28자 이내인 경우 ok
                break

    def step2(self,titlelen):
        print('='*titlelen)
        txt = '={0:^%s}=' % (titlelen-2)
        for t in self.game_info:
            print(txt.format(t))
        print('='*titlelen)

def main():
    game = NMG()
    game.step1(28)
    game.step2(28)


# 이 코드를 중심으로 구동될때만 main을 호출하고 싶다
if __name__ == '__main__':
    main()