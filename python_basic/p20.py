# 레퍼런스 카운트 ( Reference Count ) 
# 파이썬은 기본적으로 모든 것이 객체다!!
a = 1
# 1이라는 객체는 내가 만든 적이 없다
# 사실 1이란 객체는 이미 만들어져있다
# 1이란 객체를 a처럼 가르키고 있는 변수들일 몇개인지
# 즉, 몇개가 참조하고 있는지, 레퍼런스 카운트가 몇개인지
import sys # 레퍼런스 카운트를 참조하기 위해서 이걸 import
print(a,type(a),sys.getrefcount(1))
b = 1
print(b,type(b),sys.getrefcount(1))

# 참조를 끊는 방법
# -> del 를 치는 순간 사라짐
del (b)
print(sys.getrefcount(1))
del a # a라는 존재가 완전히 소멸되어서 더이상 사용이 불가하게 만듬
print(sys.getrefcount(1))