'''
4. 함수
    - 기본 문법
    - 중요 내장 함수
# 기본 문법
# def 함수이름( 인자(파라미터)들 ): 
def simplefunc(a,b,c): # 인자의 갯수는 상관없음
    c = a + b # 수행문
    return c # 리턴값들(갯수는 자유롭게), 심지어 [생략가능]
'''

# 더하기 함수 : 2개의 정수값을 받아서 더한 값을 리턴하는 sum 함수 구현
def sum (x,y): # 어차피 type은 상관없음! -> 근데 string하고 int하고 어케 구별하지?
    return x + y
# 함수의 호출 => 사용하는걸 의미함
# Call By Value : 호출하고 결과를 돌려받는다 
result = sum(1,2)
print(result)

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 

# 가변인자 : 몇개를 보낼지 모르겠으나 보낸 것 다 더해라
# 인자가 몇개 올지 알 수 없다 일단 보내는 거 다 처리해라!
# 인자 표현법을 처리 -> 가변인자 구성 
def sum2( *args ): # 덩어리가 오는거니까 loop 돌릴 생각!
    # args에서 하나씩 구성원을 뽑아서 전부 더한 값을 출력
    sum = 0
    for arg in args:
        # print(arg) #하나씩 제대로 뽑히는지 확인하기 위해서
        sum += arg # 누적합을 위해서
    #print(sum)
    return sum

print(sum2(1)) # return 값이 없으면 None이라고 나옴
print(sum2(1,2))
print(sum2(1,2,3))
print(sum2(1,2,3,4))

# 누적곱 함수를 구성하시오 => mul
def mul(*args):
    sum = 1
    for i in args:
        sum *= i
    return sum

print(mul(1,2,3,4,5,6))
print(mul(2,4,56))

# 여러값 리턴
# 가변인자로 누적합과 누적곱을 리턴하는 mix함수를  
def mix(*args):
    addsum = 0
    addmul = 1
    for i in args:
        addsum += i
        addmul *= i
    return addsum,addmul # 결과값 돌려줄때
    # return sum2(*args),mul(*args) # tuple로...값을 묶는다

print(mix(1,2,4))
print(mix(1,2,3,4))
result = mix(1,2,3,4,5,6)
print(result,type(result))

# 리턴값이 여러개면 tuple로 리턴된다
# mix(1,2,3,4,5,6) 호출해서 누적합은 a,누적곱은 b라는 변수에
# 담아서 각각 출력하시오
a,b = mix(1,2,3,4,5,6)
print(a,b)

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
print('= '*40)
# 누적합은 'a'라는 키를 통해, 누적곱은 'b'라는 키를 통해서 => dict사용
# 각각 출력 가능하게 mix()를 확장한 mixEx()를 구성하시오
def mixEx(*args):
    addsum = 0
    addmul = 1
    for i in args:
        addsum += i
        addmul *= i

    dic = dict()
    dic['a'] = addsum
    dic['b'] = addmul
    # return dic

    # return {'a':addsum,'b':addmul} # 위를 한줄로 줄이면
    return dic, {'a':addsum,'b':addmul}

rs = mixEx(1,2,3,4,5,6)
print(rs,type(rs))
# rs의 두번째 멤버 데이터 중에 키가 b인 값을 출력하시오
# rs : tuple 
# rs[1] : 이 자체가 dict이 되버림 
print(rs[1]['b']) # 이렇게 안하고 단계적으로 접근해도 상관없음

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
print('= '*40)
# 문자열을 입력받아서 앞뒤 공백을 제거하고
# [문자] 이렇게 출력해주는 함수 trimEx()를 만드셈

def trimEx( src ):
    print('[%s]' % src.strip())

trimEx('  w  e f3   ') # 중간 공백은 정규식으로 처리해서 없앤다
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
print('= '*40)
# 콘솔 출력 => print
# 자주 사용하는 함수들은 재정의해서 사용할 수 있다
# 일종의 전체 어플리케이션 기능을 통제할 수 있는 환경변수들을 정의하여서 세부 기능들도 조정이 가능
# 로그함수, 상용화시에는 isTest = False로 두어서
# 로그를 비활성화시킨다 
isTest = True
def log(msg):
    # print(msg)
    # pass # print를 한방에 다 그냥 못 쓰게도 할 수 있음 이렇게
    if isTest:
        print(msg)


log('1')
log('2')
log('3')
log('abc')

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 

def setPerson(name,age = 30, weight = 70):
    print('%s님의 나이는 %s, 몸무게는 %s이다' % (name,age,weight))

setPerson('multi')
setPerson('multi',age=20)
setPerson('multi',age=25,weight=100)
setPerson('multi',weight=19,age=25) # 기본값을 부여한 parameter들은 순서가 상관없음
# setPerson(weight=100,age=20) -> name의 값이 없기 때문에 오류!!

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 

# 사용 타이핑
# 인터프리터 언어이기 때문에 먼저 정의된 후에 사용가능하다
# test()
def test():
    print('this is test') 

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 

a = 10 # 
def check():
    a = 11 # 함수 안에서 정의된 변수, 지역변수, 함수가 호출될때만 존재
    # a가 글로벌 변수임을 지정하면 그때부터 a는 로컬변수가 아닌 전역변수를 가르키게 된다 
check()
print(a) # a = 10 ... why? 여기서 말하는 a는 check함수 안에서의 변수를 말하는게 아니니까

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 

# 함수도 수행문이 하나면 옆으로 슬 수 있다
def test1( x ): return x+'<='

print(test1('hello'))