# PersonEx Class를 구성하시오
# 속성으로 name,age가 존재
# 액션(함수)로 getName,getAge가 존재
# name,age는 생성자에서 초기화됨
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Python의 모든 클래스의 수퍼 클래스(근본이 되는 클래스)는 object라고 존재함
class PersonEx:
    
    # 1. 멤버변수
    name = None
    age = None

    # 2. 멤버함수
    # getName 함수
    def getName(self):
        return self.name
    # getAge 함수
    def getAge(self):
        return self.age

    # 3. 생성자함수
    def __init__(self,name,age):
        # print('initializing Constructor')
        self.name = name
        self.age = age

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# 요구사항 PersonEx는 그대로 두고, PersonEx2를 만들어서
# eat() 함수를 추가해달라고 요구
# PersonEx2 = PersonEx + eat()
# 위의 요구사항은 상속이란 개념으로 해결할 수 있다
# PersonEx : 부모 / PersonEx2 : 자식
# 자식은 부모의 모든 기능을 승계하고, 자식은 별도로 추가할 수 있음  
# syntax : class 자식클래스명(부모클래스명)
class PersonEx2 (PersonEx):
    def eat(self):
        print('eat() call')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# 상속 후 재정의(부모로부터 받음 함수를 재정의)
class PersonEx3(PersonEx):
    def eat(self):
        print('eat() call 1234')

# 파이값
PI = 3.14

# 내가 수행하고자하는 테스트 코드는 여기안에 위치시킴
# 내가 주인공이 될때 

if __name__ == '__main__':
    # Ex) F반 멤버
    f1 = PersonEx('홍길동',25)
    f2 = PersonEx('김철수',24)
    print([f1,f2])
    print(f1.getName(),f2.getAge())

    f2 = PersonEx2('이영희',23)
    print(f2.getName())
    f2.eat()

    f3 = PersonEx3('ABC',20)
    f3.eat()
