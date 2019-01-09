# 패키지 생성 및 가져오기, 모듈 가져오기

from p16_package import PI
# 여기에서 실행시키면 p16_package가 나오지만
# p16파일에서는 __main__이라고 나온다
# print(PI)
# 패키지는 같은 계열이나 의미를 가진 모듈들을 모아둔 디렉토리
# 하위호환(3.3이하)을 위해서 패키지를 만들면 반드시(생략가능)
# __init__.py를 생성해둔다 이 파일의 의미는 패키지 자체를 의미 
# a 밑에 b 밑에 mod.py 안에 sum함수를 가져다가 내것처럼 사용
from a.b.mod import sum
from a.b import sum2
from a.make import sum3
# 함수,클래스,변수 등 다 import할 수 있고
# 다 별칭을 쓸 수 있다 
from a import sum4
print(sum(1,2))
print(sum2(1,2))
print(sum3(1,2))
print(sum4(1,2))
####################################################################################
import a.b.mod # 이렇게 써도 아무 문제는 없음
import a.b.mod as m # 이름이 길거나 대체이름으로 사용할 경우, 별칭
print(m.sum(3,7))
import a.b as m2
print(m2.sum2(10,11))